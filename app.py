import adafruit_dht
import board
import digitalio

dht_device = adafruit_dht.DHT22(board.G4) # Algunos modelos usan G4 en lugar de D4
#dht_device = adafruit_dht.DHT22(board.D4) # Or DHT22, AM2302 etc.

try:
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    print(f"Temp={temperature}C Humidity={humidity}%")
except RuntimeError as e:
    # Reading doesn't always work on Linux, so catch the exception
    print(f"Reading error: {e.args[0]}")
