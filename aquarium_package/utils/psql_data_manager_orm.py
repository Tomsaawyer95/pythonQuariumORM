import os
"""
This module sets up the SQLAlchemy ORM connection to a PostgreSQL database using environment variables.
- Loads environment variables from a .env file for database credentials.
- Constructs the PostgreSQL connection URI.
- Initializes the SQLAlchemy engine and session maker.
- Defines the declarative base for ORM models.
Environment Variables:
    PSQL_HOST: Hostname of the PostgreSQL server.
    PSQL_PORT: Port number of the PostgreSQL server.
    PSQL_DB: Name of the PostgreSQL database.
    PSQL_USER: Username for the PostgreSQL database.
    PSQL_PASSWORD: Password for the PostgreSQL database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv


load_dotenv()
HOST = os.getenv("PSQL_HOST")
PORT = os.getenv("PSQL_PORT")
DATABASE = os.getenv("PSQL_DB")
USER = os.getenv("PSQL_USER")
PASSWORD = os.getenv("PSQL_PASSWORD")
conn_uri = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(conn_uri)
Session = sessionmaker(bind=engine)
Base = declarative_base()
