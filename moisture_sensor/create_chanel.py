import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def wake_up_channel():
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1015(i2c)
    except Exception as e:
        
        return None

def create_chanel():
    try:
        wake_up_channel()
        # Create the I2C bus
        i2c = busio.I2C(board.SCL, board.SDA)

        # Create the ADC object using the I2C bus
        ads = ADS.ADS1015(i2c)

        # Create single-ended input on channel 0
        channel = AnalogIn(ads, ADS.P0)
        return channel
    except Exception as e:
        print(f"Error creating channel: {e}")
        return None
