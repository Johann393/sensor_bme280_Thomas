from machine import Pin, I2C
from time import sleep
import bme280  # o mesmo driver serve para BMP280 também

# Configuração do barramento I2C (BitDogLab usa GP4=SDA, GP5=SCL)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=100000)

# Verifica sensores conectados
devices = i2c.scan()
print("Dispositivos I2C encontrados:", [hex(d) for d in devices])

# Inicializa o BMP280
bme = bme280.BME280(i2c=i2c)

while True:
    temp, press, hum = bme.values  # o campo de umidade virá vazio no BMP280
    print(f"Temperatura: {temp}")
    print(f"Pressão: {press}")
    print("-" * 30)
    sleep(2)
