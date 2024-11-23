import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlmodel import select
from fastapi import FastAPI, Request
from database.connection import get_session
from database.models import MoistureRecord
from typing import List
from fastapi.responses import HTMLResponse
from views.moisture import get_moisture_view

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/plants/{plant_id}/moisture-view")
def moisture_view(request: Request,plant_id: int):
    return get_moisture_view(request,plant_id)
