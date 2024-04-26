"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, declared_attr, relationship
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost:5432/postgres"
)

engine = create_async_engine(url=PG_CONN_URI)

Session = async_sessionmaker(
    bind=engine,
    autocommit=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


class User(Base):
    name = Column(String(50), nullable=True, index=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String(50), nullable=True, unique=True)

    posts = relationship("Post", back_populates="user", uselist=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, username={self.username}, email={self.email!r}"


class Post(Base):
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        unique=False,
    )
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
        unique=True,
    )

    body = Column(
        String(500),
        nullable=True,
        unique=True,
        default="",
        server_default="",
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )
