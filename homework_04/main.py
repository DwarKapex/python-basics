"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from models import (
    Base,
    User,
    Post,
    Session,
    engine,
)

from jsonplaceholder_requests import (
    fetch_users_data,
    fetch_posts_data,
)


async def create_user(
    session: AsyncSession,
    user_name: str,
    name: str | None,
    email: str | None,
):
    user = User(
        username=user_name,
        name=name,
        email=email,
    )
    session.add(user)
    await session.commit()


async def create_users(
    session: AsyncSession,
    users_data: List[dict],
) -> List[User]:
    users = [
        User(
            id=entity.get("id"),
            username=entity.get("username"),
            name=entity.get("name", ""),
            email=entity.get("email", ""),
        )
        for entity in users_data
    ]

    session.add_all(users)
    await session.commit()
    return users


async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_posts(
    session: AsyncSession,
    posts_data: List[dict],
) -> List[Post]:
    posts = [
        Post(
            id=entity.get("id"),
            user_id=entity.get("userId"),
            title=entity.get("title"),
            body=entity.get("body"),
        )
        for entity in posts_data
    ]

    session.add_all(posts)
    await session.commit()

    return posts


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with Session() as session:
        users: List[User] = await create_users(
            session,
            users_data,
        )

        posts: List[Post] = await create_posts(
            session,
            posts_data,
        )

    await engine.dispose(close=True)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
