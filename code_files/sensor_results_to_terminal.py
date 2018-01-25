import sys
import time
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085 
##import RPi.GPIO as GPIO
import Adafruit_MCP3008 as MCP

pressure_sensor = BMP085.BMP085()

mcp = MCP.MCP3008(clk=18, cs=37, miso=23, mosi=24)
print(mcp)

#GPIO.setmode(GPIO.BOARD)
##pins_in = [38, 18]
##GPIO.setup(pins_in, GPIO.IN)
##GPIO.setup(36, GPIO.OUT)


while True:
    
##    GPIO.output(36, GPIO.HIGH)
##    time.sleep(3)
##    print(GPIO.input(18))
##    time.sleep(3)
##    GPIO.output(36, GPIO.LOW)
    print(mcp.read_adc(0))
    print(mcp.read_adc(1))

    humidity, temperature = Adafruit_DHT.read_retry(11, 21)
    pressure = pressure_sensor.read_pressure()
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %').format(temperature, humidity)
    print('Pressure: {0:0.1f}').format(pressure)
    print('Temp 2: {0:0.1f}').format(pressure_sensor.read_temperature()) 
    print('Altitude: {0:0.1f}').format(pressure_sensor.read_altitude()) 