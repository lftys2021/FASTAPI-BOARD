from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    views = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    likes = relationship("Like", back_populates="post")

    comments = relationship(
        "Comment",
        back_populates="post",
        cascade="all, delete"
    )

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    posts = relationship(
        "Post",
        back_populates="author"
    )

    comments = relationship(
        "Comment",
        back_populates="author"
    )

    comment_likes = relationship(
        "CommentLike",
        back_populates="user"
    )
    

# Like 테이블 생성
class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "post_id",
            name="unique_like"
        ),
    )

    user = relationship("User")
    post = relationship("Post")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    post_id = Column(Integer, ForeignKey("posts.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")

    comment_likes = relationship(
        "CommentLike",
        back_populates="comment",
        cascade="all, delete"
    )

    parent_id = Column(
        Integer,
        ForeignKey("comments.id"),
        nullable=True
    )

    parent = relationship(
        "Comment",
        remote_side=[id],
        backref="replies"
    )

class CommentLike(Base):
    __tablename__ = "comment_likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    comment_id = Column(Integer, ForeignKey("comments.id"))

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "comment_id",
            name="unique_like"
        ),
    )

    user = relationship("User",  back_populates="comment_likes")
    comment = relationship("Comment", back_populates="comment_likes")