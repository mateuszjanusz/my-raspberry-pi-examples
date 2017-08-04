import sys
import Adafruit_DHT
import I2C_LCD_driver
from time import *


my_lcd = I2C_LCD_driver.lcd()

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    my_lcd.lcd_display_string('Temp: {0:0.1f} C'.format(temperature), 1)
    my_lcd.lcd_display_string('Humidity: {1:0.1f} %'.format(humidity), 2)


