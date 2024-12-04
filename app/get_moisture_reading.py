# from create_chanel import create_chanel
import time
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_session
from database.models import MoistureRecord
from create_records import create_moisture_record
from datetime import datetime

from aiogram.methods.send_message import SendMessage
from os import getenv
from moisture_sensor.create_chanel import create_chanel
from aiogram import Bot, Dispatcher, html

TOKEN = getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = getenv("TELEGRAM_CHAT_ID")
bot = Bot(token=TOKEN)
session = get_session()
dp = Dispatcher()

@dp.message()   
async def send_moisture_reading_alert(moisture_reading):
    bot = Bot(token=TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=f"hey something is wrong!!! the moisture level is {moisture_reading}")
    finally:
        await bot.session.close()

def read_calibration_values():
    with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/sensor_calibration.json', 'r') as f:
        return json.load(f)

calibration_values = read_calibration_values()

async def get_moisture_reading(raw_val):
    moisture_reading = abs((raw_val- int(calibration_values["max_dry_value"]))/(int(calibration_values["min_wet_value"])-int(calibration_values["max_dry_value"])))*100
    if moisture_reading > 100 or moisture_reading < 15:
        await send_moisture_reading_alert(moisture_reading)
    return round(moisture_reading, 3)




if __name__ == "__main__":
    import asyncio
    
    async def main():
        try:
            channel = create_chanel()
            value = get_moisture_reading(channel.value)
            record = MoistureRecord(moisture_level=value,plant_id=1,created_at=datetime.now(),updated_at=datetime.now())
            create_moisture_record(session,record)

        finally:
            await bot.session.close()
    
    asyncio.run(main())
    
