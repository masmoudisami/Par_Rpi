#!/usr/bin/python
import sys
import time
from gpiozero import LED # doc: https://gpiozero.readthedocs.io/

# define o GPIO a ser controlado pelo transistor na parte de gatilho
fan = LED(14)

def cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as f:
        return float(f.read())/1000


def main():
    # close fan at begining
    is_close = True
    fan.off()
    while True:
        temp = cpu_temp()
        if is_close:
            if temp > 40.0: # temperatura para ligar fan
                print(time.ctime(), temp, 'Fan ON')
                fan.on()
                is_close = False
        else:
            if temp < 39.0: # temperatura para desligar fan
                print(time.ctime(), temp, 'Fan OFF')
                fan.off()
                is_close = True

        time.sleep(2.0)
        print(time.ctime(), temp)


if __name__ == '__main__':
    main()
