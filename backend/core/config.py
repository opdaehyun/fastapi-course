import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



class Settings:
    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.1.1"

    MYSQL_USER : str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD : str = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER : str = os.getenv("MYSQL_SERVER", "localhost")
    MYSQL_PORT : str = os.getenv("MYSQL_PORT", 5432)
    MYSQL_DB : str = os.getenv("MYSQL_DB", "db_course")
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8"

settings = Settings()