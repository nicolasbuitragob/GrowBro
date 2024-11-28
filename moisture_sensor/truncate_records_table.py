import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_session
from database.models import MoistureRecord
from sqlmodel import delete, select

session = get_session()

def truncate_records_table():
    stmt = delete(MoistureRecord)
    session.exec(stmt)
    session.commit()

if __name__ == "__main__":
    truncate_records_table()
    print("Records truncated successfully")
    statement = select(MoistureRecord)
    results = session.exec(statement).all()
    print(results)
