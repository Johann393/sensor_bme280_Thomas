from machine import Pin, I2C
from time import sleep
from bmp280 import BMP280

# Inicializa I2C da BitDogLab (I2C1)
i2c = I2C(1, scl=Pin(3), sda=Pin(2))

bmp = BMP280(i2c)

# Parâmetro do filtro
N = 10  # tamanho da janela da média móvel
temps = []
press = []

print(f"Iniciando leitura filtrada (média móvel de {N} amostras)...")

while True:
    temperatura = bmp.temperature
    pressao = bmp.pressure / 100  # converte para hPa

    # adiciona novas leituras
    temps.append(temperatura)
    press.append(pressao)

    # mantém o tamanho máximo da janela
    if len(temps) > N:
        temps.pop(0)
    if len(press) > N:
        press.pop(0)

    # calcula médias
    media_t = sum(temps) / len(temps)
    media_p = sum(press) / len(press)

    # exibe
    print(f"Bruto: {temperatura:5.2f} °C | {pressao:7.2f} hPa")
    print(f"Filtrado: {media_t:5.2f} °C | {media_p:7.2f} hPa")
    print("-" * 50)
    sleep(2)
