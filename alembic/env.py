from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
import os
from dotenv import load_dotenv

load_dotenv()

config = context.config
fileConfig(config.config_file_name)

from models.database import Base

from models.dish import Dish
from models.order import Order
from models.order_dish import order_dish_association

target_metadata = Base.metadata

def run_migrations_offline():
    url = os.getenv("DATABASE_URL").replace("+asyncpg", "")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    engine = create_engine(os.getenv("DATABASE_URL").replace("+asyncpg", ""))
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()