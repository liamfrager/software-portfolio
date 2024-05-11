import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from sqlalchemy import ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    settings: Mapped["UserSettings"] = relationship(
        back_populates="user")
    list_items: Mapped[list["ListItem"]] = relationship(
        back_populates="user")


class UserSettings(db.Model):
    __tablename__ = 'user-settings'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    theme_color: Mapped[str] = mapped_column(
        String(15), nullable=True, default=None)
    default_calendar_view: Mapped[str] = mapped_column(
        String(7), default='week')
    week_start: Mapped[int] = mapped_column(Integer, default=1)
    show_future_list: Mapped[bool] = mapped_column(Boolean, default=True)
    show_overdue_list: Mapped[bool] = mapped_column(Boolean, default=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(
        back_populates="settings")


class ListItem(db.Model):
    __tablename__ = 'list-items'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(100))
    due_date: Mapped[datetime.date] = mapped_column(Date)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(
        back_populates="list_items")


class DB():
    def get_user(self, **kwargs):
        if 'id' in kwargs:
            user = db.session.execute(
                db.select(User).where(User.id == kwargs['id'])).scalar()
        elif 'email' in kwargs:
            user = db.session.execute(
                User.query.filter(User.email == kwargs['email'])).scalar()
        return user

    def add_user(self, form_data):
        new_user = User(
            email=form_data['email'],
            password=generate_password_hash(
                password=form_data['password'],
                method='pbkdf2:sha256',
                salt_length=8
            ),
            name=form_data['name']
        )
        db.session.add(new_user)
        db.session.commit()
        user_settings = UserSettings(user_id=new_user.id)
        db.session.add(user_settings)
        db.session.commit()
        return new_user


database = DB()
