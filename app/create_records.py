import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.models import Plant, MoistureRecord
from sqlmodel import Session

def create_plant(session: Session, plant: Plant) -> Plant:
    session.add(plant)
    session.commit()
    session.refresh(plant)
    return plant

def create_moisture_record(session: Session, record: MoistureRecord) -> MoistureRecord:
    session.add(record)
    session.commit()
    session.refresh(record)
    return record
