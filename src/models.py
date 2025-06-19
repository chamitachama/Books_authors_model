from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username:  Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Author(db.Model):

    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)
    # relacion

    books = relationship("Book", back_populates="author")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "books": [book.serialize() for book in self.books],
            "genre": self.genre_id
        }


class Book(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    year: Mapped[int] = mapped_column(unique=False, nullable=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"))

    # relacion

    author = relationship("Author", back_populates="books")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "author_id": self.author_id,
            "year": self.year
        }


class Genre(db.Model):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))

    # relacion

    authors = relationship("Author", back_populates="genre")

    def serialize(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "book_id": self.book_id,
            "genre_name": self.name

        }


class Favorites(db.Model):
    __tablename__ = "favorites"

    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey(
        "books.id", ondelete="CASCADE"), primary_key=True)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "book_id": self.book_id,
        }
