"""
File to initialize all database connections and make parent Base class
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush = False, bind = engine)

Base = automap_base()
Base.prepare(engine, reflect = True)

# Map classes with same names and relationships
# Only members and families for now
Members = Base.classes.members
Families = Base.classes.families
