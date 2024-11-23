import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json

from moisture_sensor.create_chanel import create_chanel
import time

channel = create_chanel()

def calibrate_moisture_sensor(type):
    values = []
    assert type in ['wet', 'dry']

    for _ in range(10):
        values.append(channel.value)
        time.sleep(0.5)

    mean = sum(values) / len(values)
    return mean

def create_calibration_file():
    default_values = {'mean_wet_value': None, 'mean_dry_value': None}
    
    # If file doesn't exist or is empty, write default values
    if not os.path.exists('sensor_calibration.json') or os.path.getsize('sensor_calibration.json') == 0:
        with open('sensor_calibration.json', 'w') as f:
            json.dump(default_values, f)
        return default_values

    # Read existing values
    with open('sensor_calibration.json', 'r') as f:
        dictValues = json.load(f)
        return dictValues

if __name__ == "__main__":
    calibration_data = create_calibration_file()  # Now returns the dict directly
    arg = sys.argv[1]
    if arg == 'wet':
        calibration_data['mean_wet_value'] = calibrate_moisture_sensor('wet')
    elif arg == 'dry':
        calibration_data['mean_dry_value'] = calibrate_moisture_sensor('dry')
    else:
        raise ValueError("Type must be 'wet' or 'dry'")
    
    print(calibration_data)
    json.dump(calibration_data, open('sensor_calibration.json', 'w'))