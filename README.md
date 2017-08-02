# Raspberry Pi Starter 

## Overview 

This is my collection of basic Raspberry pi projects and helpful resources for those getting started with the Raspberry Pi :clap:

### Contents
    
- [RPi.GPIO Python module basic documentation](#gpio-python-module-basic-documentation) 
- Projects :bulb:
    - [Blinking LED](#blinking-led)
    - [Temperature and humidity sensor](#temperature-and-humidity-sensor)
    - more coming soon...
- [Helpful resources](#helpful-resources)

## GPIO Python module basic documentation

- #### Import RPi.GPIO module
```
import RPi.GPIO as GPIO
```
- #### Specify that you are using the BOARD numbering system
```
GPIO.setmode(GPIO.BOARD)
```

- #### Disable warnings (when you have more than one script/circuit on the GPIO)
```
GPIO.setwarnings(False)
```
- #### Setup up a channel (pin_number)
```
GPIO.setup(pin_number, GPIO.IN)
GPIO.setup(pin_number, GPIO.OUT)
```
-- example
```
GPIO.setup(7, GPIO.OUT)
```
- ##### Setup multiple channels
```
pin_numbers = [7,14]    
GPIO.setup(pin_numbers, GPIO.OUT)
```
- #### Read the value of a GPIO pin

This will return either 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True
```
GPIO.input(pin_number)
```

- #### Set the output state of a GPIO pin
State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True

```
GPIO.output(pin_number, state)
```
-- example
```
GPIO.output(LedPin, GPIO.HIGH)
```

- #### Output to more than one channel
```
pin_numbers = [7,14]
GPIO.output(pin_numbers, GPIO.LOW)                # sets all to GPIO.LOW
GPIO.output(pin_numbers, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW
```

- #### Clean up 
You can clean up inividual channels or all channels like this:
```
GPIO.cleanup()
```

- #### Wiki [RPi.GPIO Python Module](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)


## Projects
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
- [Setup NOOBS](https://www.raspberrypi.org/documentation/installation/noobs.md)
- [Raspberry Pi schematics](https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/README.md)
- [About GPIO pins](https://www.raspberrypi.org/documentation/hardware/raspberrypi/gpio/README.md)
- [Raspberry Pi Pinout](https://pinout.xyz/pinout)
- [Common Pitfalls for Beginners](https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=83372)
- [Python basics](https://www.raspberrypi.org/documentation/usage/python/README.md)

