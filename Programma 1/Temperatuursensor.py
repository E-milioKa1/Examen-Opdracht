from machine import ADC
from machine import Pin
import time

# ik heb deze conversie waarde op internet moeten zoeken om naar graden om te zetten
# anders zat ik met waardes in de tienduizendtallen
temperatuur_sensor = ADC(4)
conversion_factor = 3.3/(65535)  
max_temp = 27
#27 graden is de maximum en ik heb maar 8 leds om mee te werken dus 27/8=3.3
led_temp_waarde = 3.3


leds = [Pin(2,Pin.OUT), Pin(3,Pin.OUT), Pin(4,Pin.OUT), Pin(5,Pin.OUT), Pin(6, Pin.OUT),
        Pin(7, Pin.OUT), Pin(8, Pin.OUT), Pin(9, Pin.OUT), Pin(10, Pin.OUT)]

#The temperature sensor works by delivering a voltage to the ADC4 pin that is proportional to
#the temperature. From the datasheet, a temperature of 27 degrees Celsius delivers a voltage
#of 0.706 V. With each additional degree the voltage reduces by 1.721 mV or 0.001721 V.
#The first step in converting the 16-bit temperature is to convert it back to volts, which is
#done based on the 3.3 V maximum voltage used by the Pico board.

for led in leds:
    led.off()
time.sleep(3)

while True:
    waarde = temperatuur_sensor.read_u16() * conversion_factor
    temp = 27 - (waarde -0.706)/0.001721
    print(temp)
    time.sleep(0.1)
    if temp >= 3.3:
        leds[7].on()
    else: leds[7].off()
    if temp >= 6.6:
        leds[6].on()
    else: leds[6].off()
    if temp >= 9.9:
        leds[5].on()
    else: leds[5].off()
    if temp >= 13.2:
        leds[4].on()
    else: leds[4].off()
    if temp >= 16.5:
        leds[3].on()
    else: leds[3].off()
    if temp >= 19.8:
        leds[2].on()
    else: leds[2].off()
    if temp >= 23.1:
        leds[1].on()
    else: leds[1].off()
    if temp >= 26.4:
        leds[0].on()
    else: leds[0].off()
    


    

