from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlmodel import select
from database.connection import get_session
from database.models import MoistureRecord

templates = Jinja2Templates(directory="templates")

def get_moisture_view(request: Request,plant_id: int):
    session = get_session()
    statement = select(MoistureRecord).where(MoistureRecord.plant_id == plant_id)
    results = session.exec(statement).all()
    
    return templates.TemplateResponse(
        "moisture.html",
        {
            "request": request,
            "records": results
        }
    )


