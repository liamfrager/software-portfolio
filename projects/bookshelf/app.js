import express from "express";
import pg from "pg";
import axios from "axios";

const app = express();
const port = 3000;
const db = new pg.Client({
	database: "my-bookshelf",
	user: "postgres",
	password: process.env.DB_PASSWORD,
	host: "localhost",
	port: "5432",
});

db.connect();

app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

// Load home page (load all books on the shelf)
app.get("/", async (req, res) => {
	const books = await db.query("SELECT * FROM bookshelf ORDER BY date_added DESC");
	res.render("index.ejs", { books: books.rows });
});

// Sort bookshelf.
app.post("/", async (req, res) => {
	let order = req.body.order;
	const books = await db.query(`SELECT * FROM bookshelf ORDER BY ${order}`);
	res.render("index.ejs", { books: books.rows });
});

// Load data for a book.
app.get("/bookshelf", async (req, res) => {
	const isbn = req.query.isbn;
	const dbResponse = await db.query("SELECT * FROM bookshelf WHERE isbn=$1", [isbn]);
	res.render("bookshelf.ejs", { book: dbResponse.rows[0] });
});

// Update notes & rating for a book.
app.post("/notes", async (req, res) => {
	const isbn = req.body.isbn;
	const notes = req.body.notes;
	const rating = req.body.rating;
	const dbResponse = await db.query("UPDATE bookshelf SET notes=$1, rating=$2 WHERE isbn=$3", [notes, rating, isbn]);
	res.redirect(`/bookshelf?isbn=${isbn}`);
});

// Remove a book from the bookshelf.
app.post("/delete", async (req, res) => {
	const isbn = req.body.isbn;
	const dbResponse = await db.query("DELETE FROM bookshelf WHERE isbn=$1", [isbn]);
	res.redirect("/")
});

// Load the new book page.
app.get("/new-book", async (req, res) => {
	res.render("new-book.ejs", {
		heading: "Search for a book"
	});
});

// Search API for book data and display it for user.
app.post("/search-book", async (req, res) => {
	const isbn = req.body.isbn;
	const dbResponse = await db.query("SELECT * FROM bookshelf WHERE isbn=$1", [isbn]);
	const bookAlreadyOnShelf = dbResponse.rowCount !== 1 ? false : true;
	const response = await axios.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn);
	const data = response.data.totalItems === 1 ? response.data.items[0].volumeInfo : {
		heading: "Book not found. Try again.",
		authors: [""],
		cover: "",
	};
	res.render("new-book.ejs", {
		heading: "Book found!",
		isbn: isbn,
		title: data.title,
		author: data.authors[0],
		cover: data.imageLinks ? data.imageLinks.thumbnail : "https://bookcart.azurewebsites.net/Upload/Default_image.jpg",
		bookAlreadyOnShelf: bookAlreadyOnShelf
	});
});

// Add book to shelf (or redirect to the book if already on the shelf).
app.post("/add-book", async (req, res) => {
	const isbn = req.body.isbn;
	const response = await axios.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn);
	const data = response.data.items[0].volumeInfo
	const checkIfOnShelf = await db.query("SELECT * FROM bookshelf WHERE isbn=$1", [isbn]);
	if (checkIfOnShelf.rowCount !== 1) {
		const dbResponse = await db.query(
			"INSERT INTO bookshelf (isbn, title, author, cover, notes, date_added) VALUES ($1, $2, $3, $4, $5, $6)",
			[isbn, data.title, data.authors[0], data.imageLinks ? data.imageLinks.thumbnail : "https://bookcart.azurewebsites.net/Upload/Default_image.jpg", data.description, new Date()]
		);
	}
	res.redirect(`/bookshelf?isbn=${isbn}`);
});

// Runs server locally
app.listen(port, () => {
	console.log(`Server is running on port ${port}.`);
});