import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlmodel import select
from fastapi import FastAPI, Request
from database.connection import get_session
from database.models import MoistureRecord
from typing import List
from fastapi.responses import HTMLResponse
from views.moisture import get_moisture_view,get_moisture_table
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import uvicorn
from contextlib import asynccontextmanager


TOKEN = getenv("TELEGRAM_BOT_TOKEN")
dp = Dispatcher()

@asynccontextmanager
async def lifespan(app: FastAPI):
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    asyncio.create_task(dp.start_polling(bot))
    yield
    await bot.session.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/plants/{plant_id}/moisture-view")
def moisture_view(request: Request,plant_id: int):
    return get_moisture_view(request,plant_id)

@app.get("/plants/{plant_id}/moisture-table")
def moisture_table(request: Request,plant_id: int):
    return get_moisture_table(request,plant_id)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    session = get_session()
    query = select(MoistureRecord.moisture_level,
                   MoistureRecord.created_at,
                   MoistureRecord.plant_id).order_by(MoistureRecord.created_at.desc()).limit(1)
    
    result = session.exec(query).first()
    
    if result:
        moisture_level = result.moisture_level
        created_at = result.created_at
        created_at_formatted = created_at.strftime("%Y-%m-%d %H:%M:%S")
        await message.answer(f"Hello! The moisture percentage for your plant is {moisture_level} and the last record was taken at {created_at_formatted}")
    else:
        await message.answer("No moisture records found!")
    
    session.close()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)