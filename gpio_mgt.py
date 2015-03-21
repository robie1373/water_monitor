import platform
import re

if re.match("arm", platform.machine()):
  try:
    import RPi.GPIO as GPIO
  except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

class GPIOManagement():

  """ setup GPIO related things like pins and events. """

  def __init__(self):
    self._relay_closed  = GPIO.HIGH
    self._relay_open    = GPIO.LOW
    self._flow_sensor   = 7
    self._override      = 11
    self._solenoid      = 16
    self._heat_tape     = 18
    self._grean_led     = 13
    self._red_led       = 15

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(self._flow_sensor,   GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(self._override,      GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(self._solenoid,      GPIO.OUT)
    GPIO.output(self._solenoid,     GPIO.HIGH)

    GPIO.setup(self._heat_tape,     GPIO.OUT)
    GPIO.output(self._heat_tape,    GPIO.HIGH)
    
    GPIO.setup(self._green_led,     GPIO.OUT)
    GPIO.output(self._green_led,    GPIO.LOW)
    
    GPIO.setup(self._red_led,       GPIO.OUT)
    GPIO.output(self._red_led,      GPIO.LOW)
    
  def cleanup(self):
    GPIO.cleanup()

  def flow_sensor():
      doc = "flow_sensor pin"
      def fget(self):
          return self._flow_sensor
      def fset(self, value):
          self._flow_sensor = value
      def fdel(self):
          del self._flow_sensor
      return locals()
  flow_sensor = property(**flow_sensor()) 

  def override():
      doc = "override pin"
      def fget(self):
          return self._override
      def fset(self, value):
          self._override = value
      def fdel(self):
          del self._override
      return locals()
  override = property(**override())

  def solenoid():
      doc = "solenoid pin"
      def fget(self):
          return self._solenoid
      def fset(self, value):
          self._solenoid = value
      def fdel(self):
          del self._solenoid
      return locals()
  solenoid = property(**solenoid())

  def relay_closed():
      doc = "The relay_closed property."
      def fget(self):
          return self._relay_closed
      def fset(self, value):
          self._relay_closed = value
      def fdel(self):
          del self._relay_closed
      return locals()
  relay_closed = property(**relay_closed())

  def relay_open():
      doc = "The relay_open property."
      def fget(self):
          return self._relay_open
      def fset(self, value):
          self._relay_open = value
      def fdel(self):
          del self._relay_open
      return locals()
  relay_open = property(**relay_open())

  def set_green_led(self, state):
    if state == "on":
      GPIO.output(self._green_led, HIGH)
    elif state == "off":
      GPIO.output(self._green_led, LOW)
    else:
      raise ValueError("State must be 'on' or 'off'")

  def set_red_led(self, state):
    if state == "on":
      GPIO.output(self._red_led, HIGH)
    elif state == "off":
      GPIO.output(self._red_led, LOW)
    else:
      raise ValueError("State must be 'on' or 'off'")
