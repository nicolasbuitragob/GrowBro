from create_chanel import create_chanel
import time
import json
channel = create_chanel()


def read_calibration_values():
    with open('sensor_calibration.json', 'r') as f:
        return json.load(f)

calibration_values = read_calibration_values()

def get_moisture_reading(raw_val):
    print(raw_val)
    per_val = abs((raw_val- calibration_values["mean_dry_value"])/(calibration_values["mean_wet_value"]-calibration_values["mean_dry_value"]))*100
    return round(per_val, 3)
    
while True:
    get_moisture_reading(channel.value)
    time.sleep(0.5)
