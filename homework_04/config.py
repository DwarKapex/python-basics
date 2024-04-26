from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_ECHO = True
DB_URL = "postgresql+psycopg://user:example@localhost:5432/blog"
