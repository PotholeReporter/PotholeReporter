#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
# Copyright (C) 2018  Seeed Technology Co.,Ltd.
'''
This is the code for
    - `Grove - Sound Sensor <https://www.seeedstudio.com/Grove-Sound-Sensor-p-752.html>`_

Examples:

    .. code-block:: python

        import time
        from grove.grove_sound_sensor import GroveSoundSensor

        # connect to alalog pin 2(slot A2)
        PIN = 2

        sensor = GroveSoundSensor(PIN)

        print('Detecting sound...')
        while True:
            print('Sound value: {0}'.format(sensor.sound))
            time.sleep(.3)
'''
import math
import time
from grove.adc import ADC
import os

#__all__ = ['GroveSoundSensor']

class VibrationSensor(object):
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def vibration(self):
        '''
        Get the strength value

        Returns:
            (int): ratio, 0(0.0%) - 1000(100.0%)
        '''
        value = self.adc.read(self.channel)
        return value

#Grove = GroveSoundSensor


def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.ADC)
    pin = sh.argv2pin()

    sensor = VibrationSensor(pin)

    print('Detecting vibration...')
    while True:
	vib = sensor.vibration
	if vib > 500:
		print('Pothole detected!')
		print('Vibration strength %: {0}'.format(sensor.vibration/10))
		os.system('python /root/grove.py/grove/sendemail.py')
		os.system('python /root/grove.py/grove/sendmms.py')
	        time.sleep(.5)

if __name__ == '__main__':
    main()
