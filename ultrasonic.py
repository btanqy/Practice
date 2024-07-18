from dht import DHT11
import machine
from machine import Pin
from time import sleep

pin = Pin(15, Pin.IN, Pin.PULL_UP)
d = DHT11(pin)

while True:
    try:
        sleep(2)
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        temp_f = temp * (9 / 5) + 32.0
        print("Temperature: %3.1f C" % temp)
        print("Temperature: %3.1f F" % temp_f)
        print("Humidity: %3.1f %%" % hum)
    except OSError as e:
        print("Failed to read sensor.")
