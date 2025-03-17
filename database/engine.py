from sqlalchemy.ext.asyncio import create_async_engine
from database.config import DATABASE_URL

# Создаем асинхр. движок SQLAlchemy:
engine = create_async_engine(DATABASE_URL, echo=True) # echo=True для логов SQL-запросов
