# Raspberry Pi Starter

## Overview 

This is a collection of basic Raspberry pi projects for for those who wish to start learning programming with the Raspberry Pi

### Contents
    
    
- [Blinking LED](#blinking-led)
- [Temperature and humidity sensor](#temperature-and-humidity-sensor)
- more coming soon...
- [Helpful resources](#helpful-resources)

## Blinking LED
code: *blink_led.py*

![Blinking led project wiring diagram](breadboards/blink_led.png?raw=true "Blinking led project wiring diagram")

Execute Python program in terminal:
``` 
python blink_led.py 
```



## Temperature and humidity sensor
* sensor DHT11
* code: *temp_humid_sensor.py*


![DHT11 project wiring diagram](breadboards/temp_humid.png?raw=true "DHT11 project wiring diagram")


#####  Install the Adafruit DHT11 library first
1. Clone a repository 
``` 
git clone https://github.com/adafruit/Adafruit_Python_DHT.git 
```
2. Install library
```
cd Adafruit_Python_DHT
sudo apt-get install build-essential python-dev
sudo python setup.py install
```
2. Run code *temp_humid_sensor.py*
``` 
python temp_humid_sensor.py 
```

> credits: circuit.basics.com


## Helpful Resources
- [What you need to start with Raspberry Pi](https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=83446)
- [Getting Started with the Raspberry Pi](https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=4751)
- [Raspberry Pi Pinout](https://pinout.xyz/pinout)
- [Common Pitfalls for Beginners](https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=83372)

