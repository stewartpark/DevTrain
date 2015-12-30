try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
except:
    class GPIO(object):
        """Fake class to test it on PC."""
        OUT = IN = 0
        @staticmethod
        def setup(*args):
            pass
        @staticmethod
        def output(*args):
            pass
        @staticmethod
        def start(*args):
            pass
        @staticmethod
        def stop(*args):
            pass
        @staticmethod
        def PWM(*args):
            return GPIO

import os

# Hardware config
PIN_CTRL = 11
PWM = None

FORWARD_SLOW =  79
BACKWARD_SLOW = 37
FORWARD_FAST = 100
BACKWARD_FAST = 0

def go(dutycycle):
    global PWM
    if PWM:
        PWM.stop()
        PWM = None
    GPIO.setup(PIN_CTRL, GPIO.OUT)
    PWM = GPIO.PWM(PIN_CTRL, 30)
    PWM.start(dutycycle)


def stop():
    global PWM
    GPIO.setup(PIN_CTRL, GPIO.IN)
    if PWM:
        PWM.stop()
        PWM = None

def choo():
    os.system("play sounds/choo.mp3 &")  # needs sox installed.
