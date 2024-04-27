import time
import machine
from micropyGPS import MicropyGPS
from machine import Pin, I2C
import ssd1306
#import ssd1306
import _thread
import time
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Carte', 0, 0)  # Afficher les deux mots ''
oled.text('ESP32', 0, 10)
oled.show()

def main():
    #♦i2c = machine.I2C(scl=machine.Pin(2), sda=machine.Pin(4))
   # dsp = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    uart = machine.UART(1, rx=16, tx=17, baudrate=9600, bits=8, parity=None, stop=1, timeout=5000, rxbuf=1024)

    gps = MicropyGPS()

    while True:
      buf = uart.readline()
      if uart.any():
       for char in buf:
         gps.update(chr(char))  # Note the conversion to to chr, UART outputs ints normally

       print('UTC Timestamp:', gps.timestamp)
       print('Date:', gps.date_string('long'))
       print('Latitude:', gps.latitude)
       print('Longitude:', gps.longitude_string())
       print('Horizontal Dilution of Precision:', gps.hdop)
       print('Altitude:', gps.altitude)
       print('Satellites:', gps.satellites_in_use)
       print()
neo-m6 gps
       oled.fill(0)
       y = 0
       dy = 10
       oled.text("{}".format(gps.date_string('s_mdy')), 0, y)
       oled.text("Sat:{}".format(gps.satellites_in_use), 80, y)
       y += dy
       oled.text("{:02d}:{:02d}:{:02.0f}".format(gps.timestamp[0], gps.timestamp[1], gps.timestamp[2]),  0, y)
       y += dy
       oled.text("Lat:{}{:3d}'{:02.4f}".format(gps.latitude[2], gps.latitude[0], gps.latitude[1]),  0, y)
       y += dy
       oled.text("Lon:{}{:3d}'{:02.4f}".format(gps.longitude[2], gps.longitude[0], gps.longitude[1]),  0, y)
       y += dy
       oled.text("Alt:{:0.0f}ft".format(gps.altitude * 1000 / (12*25.4)),  0, y)
       y += dy
       oled.text("HDP:{:0.2f}".format(gps.hdop),  0, y)
       oled.show()

def startGPSthread():
    _thread.start_new_thread(main, ())

if __name__ == "__main__":
  print('...running main, GPS testing')
  main()
