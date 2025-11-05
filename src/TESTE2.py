from machine import Pin, I2C
import ssd1306
import time

# BitDogLab I2C: SDA = GP2, SCL = GP3
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)

# OLED 128x64 I2C
WIDTH = 128
HEIGHT = 64
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:
    devices = i2c.scan()

    oled.fill(0)
    oled.text("I2C Scanner", 0, 0)

    if len(devices) == 0:
        oled.text("No devices", 0, 20)
    else:
        oled.text("Found:", 0, 20)
        y = 35
        for d in devices:
            oled.text(hex(d), 0, y)
            y += 10

    oled.show()
    time.sleep(2)
