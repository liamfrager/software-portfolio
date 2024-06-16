# Liam Frager Software Portfolio

## Projects

- [To-Do List](#to-do-list)
- [Space Invaders](#space-invaders)
- [Bookshelf](#bookshelf)
- [AVL Tree](#avl-tree)

---

## To-Do List
A To-do list web app with user authentication, multiple lists, and a calendar view.

### Login page
Implements secure user authentication with password hashing.

![alt text](./images/to-do-list/login.png)

### List view
Show lists for "Today", "This Week", and "This Month". Also features optional "Overdue" and "Future" lists.

![alt text](./images/to-do-list/lists.png)

### Calendar view
Scroll forward and backward in a calendar of your to-do items. Viewing options include...

By week:

![alt text](./images/to-do-list/week.png)

By month:

![alt text](./images/to-do-list/month.png)

By year:

![alt text](./images/to-do-list/year.png)

### Edit
Users can edit a list to add more items, change dates, and delete items.

![alt text](./images/to-do-list/edit.png)

### Settings
Comes with a settings page with the following features:
- toggle optional lists in list view
- change the default calendar view
- choose whether the week starts on Monday or Sunday
- apply a theme color to the whole application
- logout
- delete account

![alt text](./images/to-do-list/settings.png)

### Mobile compatible
The web app is responsive and can be used on both desktop and mobile.

![alt text](./images/to-do-list/mobile.png)

---

## Space Invaders
A desktop remake of the original space invaders game written in python.

### Starting screen
Uses ASCII art for a dramatic title screen.

![alt text](./images/space-invaders/start.png)

### Mystery UFO?!
What will happen when you shoot the ufo? (You get bonus points).

![alt text](./images/space-invaders/ufo.png)

### Death
The player explodes and loses a life when hit by an alien's laser.

![alt text](./images/space-invaders/death.png)

### Game Over
When you lose all your lives, the game is over. The high score is updated.

![alt text](./images/space-invaders/game_over.png)

---

## Bookshelf
A web app that allows users to store their favorite books, take notes, and give a rating.

### View all your books
A grid display of all the books on the user's bookshelf.

![alt text](./images/bookshelf/books.png)

### Sort books
The filter button allows the user to sort their bookshelf by title, author, rating, time added, or ISBN.

![alt text](./images/bookshelf/filter.png)

### Book details
The user can view a book's details, take notes, give it a rating out of five star. This is also where the user can remove a book from their shelf.

![alt text](./images/bookshelf/book.png)

### Search for a book by ISBN number
The user can add a book by searching with an ISBN number.

![alt text](./images/bookshelf/search.png)

### Mobile compatible
The web app is responsive and can be used on both desktop and mobile.

![alt text](./images/bookshelf/mobile.png)

---

## AVL Tree
An python implementation of an Adelson-Velsky-Landis binary search tree (AVL tree).

### Tree visualization
Includes a custom `__repr__` method that prints a visual representation of a node and up to three generations of its decendents.

![alt text](./images/avl-tree/full_tree.png)

### Functionality
Includes the following methods:
- `insert`: add a node to the tree.
- `delete`: remove a node from the tree.
- `exists`: returns a bool indicating whether a node with the given value exists in the tree.
- `find`: returns a node in the tree with the given value if there is one.

Includes the following properties:
- `max`: returns the node with the largest value.
- `min`: returns the node with the smallest value.
- `values`: returns all the values in the tree as a numerically sorted list.

### Known limitations
- `__repr__` method only works with values between 0 and 999 inclusive.
- Tree will not create a node with a value that is already in the tree (but one can insert a node whose child has a value that is already in the tree.)