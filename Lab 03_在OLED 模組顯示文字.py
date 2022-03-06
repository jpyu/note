from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(scl=Pin(22), sda=Pin(21)) #ESP32:GPIO22 D2:GPIO21
#i2c = I2C(scl=Pin(5), sda=Pin(4)) #D1-mini:GPIO5 D2:GPIO4

oled = SSD1306_I2C(128, 64, i2c)

oled.text("I love PYTHON!", 0, 0)

oled.fill(0)   #fill entire screen with colour=0
oled.fill_rect(0, 0, 32, 32, 1) # draw a solid rectangle 0,0 to 32,32, colour=1
oled.fill_rect(2, 2, 28, 28, 0)
oled.vline(9, 8, 22, 1)
oled.vline(16, 2, 22, 1)
oled.vline(23, 8, 22, 1)
oled.fill_rect(26, 24, 2, 4, 1)
oled.text('MicroPython', 40, 0, 1)
oled.text('SSD1306', 40, 12, 1)
oled.text('OLED 128x64', 40, 24, 1)
oled.show()