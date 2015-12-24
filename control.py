try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
except:
    class GPIO(object):
        """Fake class to test it on PC."""
        OUT = IN = 0
        @staticmethod
        def setup(cls, *args):
            pass
        @staticmethod
        def output(cls, *args):
            pass

# Hardware config
PIN_CTRL = 11
PWM = None

FORWARD_SLOW =  49
BACKWARD_SLOW = 47
FORWARD_FAST = 100
BACKWARD_FAST = 0

def go(dutycycle):
    global PWM
    if PWM:
        PWM.stop()
    GPIO.setup(PIN_CTRL, GPIO.OUT)
    PWM = GPIO.PWM(PIN_CTRL, 50)
    PWM.start(dutycycle)


def stop():
    global PWM
    GPIO.setup(PIN_CTRL, GPIO.IN)
    if PWM:
        PWM.stop()
