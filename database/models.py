from datetime import datetime

from sqlmodel import Field, SQLModel

class Plant(SQLModel, table=True):
    __tablename__ = "plants" 

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    created_at: datetime = Field(default=datetime.now)
    updated_at: datetime = Field(default=datetime.now)

class MoistureRecord(SQLModel, table=True):
    __tablename__ = "moisture_records"
    id: int | None = Field(default=None, primary_key=True)
    plant_id: int = Field(index=True, foreign_key="plants.id")
    moisture_level: float = Field(index=True)
    created_at: datetime = Field(default=datetime.now)
    updated_at: datetime = Field(default=datetime.now)