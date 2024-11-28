from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlmodel import select
from database.connection import get_session
from database.models import MoistureRecord
import pandas as pd


templates = Jinja2Templates(directory="templates")


def get_moisture_data(plant_id):
    session = get_session()
    query = select(MoistureRecord.moisture_level,
                   MoistureRecord.created_at).where(MoistureRecord.plant_id == plant_id)
    
    results = session.exec(query).all()
    return results

    

def get_moisture_view(request: Request,plant_id: int):
    data = get_moisture_data(plant_id=plant_id)
    df = pd.DataFrame(data)
    dates = df['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S').tolist()
    moisture_values = df['moisture_level'].tolist()
    
    return templates.TemplateResponse(
        "moisture.html",
        {
            "request": request,
            "dates": dates,
            "moisture_values": moisture_values
        }
    )


