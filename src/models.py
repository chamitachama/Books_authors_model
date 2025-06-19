from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username:  Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    firstname:  Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)
    lastname:  Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email

            # do not serialize the password, its a security breach
        }


class Follower(db.Model):
    user_from_id: Mapped[int] = mapped_column(ForeignKey(
        "user.id"), primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id

            # do not serialize the password, its a security breach
        }


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id

            # do not serialize the password, its a security breach
        }


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    comment_text: Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "post_id": self.post_id,
            "comment_text": self.comment_text

            # do not serialize the password, its a security breach
        }


class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    type: Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))

    def serialize(self):
        return {
            "id": self.id,
            "url": self.url,
            "type": self.type,
            "post_id": self.post_id

            # do not serialize the password, its a security breach
        }
