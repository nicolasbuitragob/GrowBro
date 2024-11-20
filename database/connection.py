from typing import Annotated
from sqlmodel import Session, create_engine
from dotenv import load_dotenv
import os
load_dotenv()


def get_session():
    sqlite_file_name = os.getenv('DB_FILE')
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, connect_args=connect_args)
    session = Session(engine)
    return session
    
