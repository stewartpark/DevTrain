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


def go(velocity=1.0):
    global PWM
    if PWM:
        PWM.stop()
    GPIO.setup(PIN_CTRL, GPIO.OUT) 
    PWM = GPIO.PWM(PIN_CTRL, 50)
    PWM.start(int(75 + (20 * velocity)))


def stop():
    global PWM
    GPIO.setup(PIN_CTRL, GPIO.IN)
    if PWM:
        PWM.stop()
