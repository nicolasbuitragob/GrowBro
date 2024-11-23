from typing import Annotated
from sqlmodel import Session, create_engine
from dotenv import load_dotenv
import os
load_dotenv()
import sys

def get_session():
    sqlite_file_name = os.getenv('DB_FILE')
    sqlite_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + sqlite_file_name
    sqlite_url = f"sqlite:///{sqlite_file_path}"
    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, connect_args=connect_args)
    session = Session(engine)
    return session
    
