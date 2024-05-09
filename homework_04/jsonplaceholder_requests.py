"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import dataclasses
import logging

import aiohttp

PLACEHOLDER_URL = "https://jsonplaceholder.typicode.com"
USERS_DATA_URL = f"{PLACEHOLDER_URL}/users"
POSTS_DATA_URL = f"{PLACEHOLDER_URL}/posts"

log = logging.getLogger(__name__)


async def fetch_json(url: str) -> dict:
    log.info("Fetch data from %s", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def fetch_users_data():
    response: dict = await fetch_json(USERS_DATA_URL)
    return response


async def fetch_posts_data() -> dict:
    response: dict = await fetch_json(POSTS_DATA_URL)
    return response
