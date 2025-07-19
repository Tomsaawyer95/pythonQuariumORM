import os

from aquarium_package.models import Type, Sexe

import pandas as pd
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, Boolean, ForeignKey
from dotenv import load_dotenv


load_dotenv()
HOST = os.getenv("PSQL_HOST")
PORT = int(os.getenv("PSQL_PORT"))
DATABASE = os.getenv("PSQL_DB")
USER = os.getenv("PSQL_USER")
PASSWORD = os.getenv("PSQL_PASSWORD")
conn_uri = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(conn_uri)
metadata = MetaData()

Table(
    "fishs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("type_fish", String),
    Column("sexe", String),
    Column("age", Integer),
    Column("pv", Integer),
    Column("fish_aquarium_id", Integer),
    Column("is_alive", Boolean)
)

Table(
    "algues",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("pv",Integer),
    Column("age", Integer),
    Column("algue_aquarium_id", Integer),
    Column("is_alive", Boolean)
)

Base.metadata.create_all(engine)