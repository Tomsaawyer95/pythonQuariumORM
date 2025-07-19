import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv


load_dotenv()
HOST = os.getenv("PSQL_HOST")
PORT = int(os.getenv("PSQL_PORT"))
DATABASE = os.getenv("PSQL_DB")
USER = os.getenv("PSQL_USER")
PASSWORD = os.getenv("PSQL_PASSWORD")
conn_uri = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(conn_uri)
Session = sessionmaker(bind=engine)
Base = declarative_base()
