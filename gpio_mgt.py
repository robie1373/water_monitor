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

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(self._flow_sensor,   GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(self._override,      GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(self._solenoid,      GPIO.OUT)
    GPIO.output(self._solenoid,     GPIO.HIGH)
    
    GPIO.setup(self._heat_tape,     GPIO.OUT)
    GPIO.output(self._heat_tape,    GPIO.HIGH)
    
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
