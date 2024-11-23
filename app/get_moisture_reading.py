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
from moisture_sensor.create_chanel import create_chanel

session = get_session()


def read_calibration_values():
    with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/sensor_calibration.json', 'r') as f:
        return json.load(f)

calibration_values = read_calibration_values()

def get_moisture_reading(raw_val):
    per_val = abs((raw_val- calibration_values["mean_dry_value"])/(calibration_values["mean_wet_value"]-calibration_values["mean_dry_value"]))*100
    return round(per_val, 3)
    


if __name__ == "__main__":
    channel = create_chanel()
    value = get_moisture_reading(channel.value)
    record = MoistureRecord(moisture_level=value,plant_id=1,created_at=datetime.now(),updated_at=datetime.now())
    create_moisture_record(session,record)
    

