from flow_counter import FlowCounter
from readings_calculator import ReadingsCalculator
from solenoid import Solenoid

import platform
import re

if re.match("arm", platform.machine()):
  try:
    import RPi.GPIO as GPIO
  except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

  from gpio_mgt import GPIOManagement
  platform = "rpi"

class ControllerConfig():

  """Configuration settings for the flow_monitor instance. 
  Includes moving_avg_interval which is the window (in seconds) over which we want to average. defaults to 5 min
  Also reading_interval which is number of seconds to take between readings."""
  
  def __init__(self):
    self._moving_avg_interval   = 300 # seconds
    self._reading_interval      = 5 # seconds
    self._shutoff_value         = 1 # gallon
    self._emergency_status      = False

    self._flow_counter            = FlowCounter()
    self._readings_calculator     = ReadingsCalculator()

    if platform == "rpi":
      self._solenoid              = Solenoid()
      self._gpio                  = GPIOManagement()
      self._gpio.set_green_led("on")
      try:
        GPIO.add_event_detect(self._gpio.flow_sensor, GPIO.RISING, callback=self._flow_counter.flow_rate_callback, bouncetime=100)
      except RuntimeError as err:
        if re.match(err.__str__(), "Conflicting edge detection already enabled for this GPIO channel"):
          print "GPIO already configured elsewhere."
          self._gpio.cleanup()
        else:
          raise err
    else:
      class GPIOFake:
        def set_green_led(self, msg):
          pass
        def set_red_led(self, msg):
          pass

      self._gpio            = GPIOFake()
      self._solenoid        = None

  def flow_counter():
      doc = "The flow_counter property."
      def fget(self):
          return self._flow_counter
      def fset(self, value):
          self._flow_counter = value
      def fdel(self):
          del self._flow_counter
      return locals()
  flow_counter = property(**flow_counter())

  def readings_calculator():
      doc = "The readings_calculator property."
      def fget(self):
          return self._readings_calculator
      def fset(self, value):
          self._readings_calculator = value
      def fdel(self):
          del self._readings_calculator
      return locals()
  readings_calculator = property(**readings_calculator())

  def solenoid():
      doc = "The solenoid property."
      def fget(self):
          return self._solenoid
      def fset(self, value):
          self._solenoid = value
      def fdel(self):
          del self._solenoid
      return locals()
  solenoid = property(**solenoid())

  def gpio():
      doc = "The gpio property."
      def fget(self):
          return self._gpio
      def fset(self, value):
          self._gpio = value
      def fdel(self):
          del self._gpio
      return locals()
  gpio = property(**gpio()) 

  def moving_avg_interval():
      doc = "The moving_avg_interval value."
      def fget(self):
          return self._moving_avg_interval
      def fset(self, value):
          self._moving_avg_interval = value
      def fdel(self):
          del self._moving_avg_interval
      return locals()
  moving_avg_interval = property(**moving_avg_interval()) 

  def reading_interval():
      doc = "The reading_interval property."
      def fget(self):
          return self._reading_interval
      def fset(self, value):
          self._reading_interval = value
      def fdel(self):
          del self._reading_interval
      return locals()
  reading_interval = property(**reading_interval()) 

  def shutoff_value():
      doc = "The shutoff_value property."
      def fget(self):
          return self._shutoff_value
      def fset(self, value):
          self._shutoff_value = value
      def fdel(self):
          del self._shutoff_value
      return locals()
  shutoff_value = property(**shutoff_value())

  def emergency_status():
      doc = "The emergency_status property."
      def fget(self):
          return self._emergency_status
      def fset(self, value):
          self._emergency_status = value
      def fdel(self):
          del self._emergency_status
      return locals()
  emergency_status = property(**emergency_status()) 
  
  def set_emergency_status(self, state):
    if state == True:
      self.emergency_status = True
      self.gpio.set_green_led("off")
      self.gpio.set_red_led("on")
    elif state == False:
      self.emergency_status = False
      self.gpio.set_green_led("on")
      self.gpio.set_red_led("off")
    else:
      raise ValueError("Emergency status must be True or False")
