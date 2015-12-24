try:
    import RPi.GPIO as GPIO
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

PIN_CTRL = 11


def go_forward():
    GPIO.setup(PIN_CTRL, GPIO.OUT)
    GPIO.output(PIN_CTRL, 1)


def go_backward():
    GPIO.setup(PIN_CTRL, GPIO.OUT)
    GPIO.output(PIN_CTRL, 0)


def stop():
    GPIO.setup(PIN_CTRL, GPIO.IN)
