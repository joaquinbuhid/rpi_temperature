import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(D4) # Or DHT22, AM2302 etc.

try:
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    print(f"Temp={temperature}C Humidity={humidity}%")
except RuntimeError as e:
    # Reading doesn't always work on Linux, so catch the exception
    print(f"Reading error: {e.args[0]}")
