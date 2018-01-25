import sys
import Adafruit_DHT
import I2C_LCD_driver
from time import *

my_lcd = I2C_LCD_driver.lcd()
while True:
    print('printing')
    my_lcd.lcd_display_string("hello world", 2, 3)