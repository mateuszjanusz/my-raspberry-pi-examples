# Simple example that displays the temperature and humidity to terminal (sensor DHT11)

# Install the Adafruit DHT11 library first: 
# 1. git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# 2. cd Adafruit_Python_DHT
# 3. sudo apt-get install build-essential python-dev
# 4. sudo python setup.py install


import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)