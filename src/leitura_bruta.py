from machine import Pin, I2C
from time import sleep
from bmp280 import BMP280

# Configuração I2C da BitDogLab
# (SDA = GP4, SCL = GP5 → I2C0)
i2c = I2C(1, scl=Pin(3), sda=Pin(2))

# Cria objeto do sensor
bmp = BMP280(i2c=i2c)

print("Iniciando leitura do BMP280...")

while True:
    temperatura = bmp.temperature      # em °C
    pressao = bmp.pressure / 100        # em hPa

    print(f"Temperatura: {temperatura:.2f} °C | Pressão: {pressao:.2f} hPa")
    sleep(2)
