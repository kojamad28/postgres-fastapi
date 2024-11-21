from dotenv import dotenv_values
from sqlalchemy import URL
from sqlmodel import SQLModel, Session, create_engine


config = dotenv_values("api/.env.development")
#config = dotenv_values("api/.env")


DEBUG = config.get("DEBUG", "false").lower() == "true"


db_url = URL.create(
        "postgresql+psycopg",
        username=config["DATABASE_USER"],
        password=config["DATABASE_PASSWORD"],  # plain (unescaped) text
        host=config.get("DATABASE_HOST", "postgres"),
        port=config.get("DATABASE_PORT", "5432"),
        database=config.get("DATABASE_DB", "postgres"),
        query={"options": f"-c search_path={config.get('DATABASE_SCHEMA', 'public')}"},
)
connect_args = {}
engine = create_engine(db_url, echo=DEBUG, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
