import platform
import re
import time
import sys
from flow_reader import FlowReader
from controller_config import ControllerConfig
from flow_counter import FlowCounter
from threading import Timer
from readings_calculator import ReadingsCalculator
from flow_switcher import FlowSwitcher
from solenoid import Solenoid

if re.match("arm", platform.machine()):
  try:
    import RPi.GPIO as GPIO
  except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

  from gpio_mgt import GPIOManagement
  platform = "rpi"

class Main():
  def __init__(self):
    self._config                  = ControllerConfig()
    self._flow_reader             = FlowReader(self._config)
    self._flow_counter            = FlowCounter()
    self._readings_calculator     = ReadingsCalculator()
    self._flow_switcher           = FlowSwitcher(self._config)

    if platform == "rpi":
      self._solenoid                = Solenoid()
      self._gpio                  = GPIOManagement()
      try:
        GPIO.add_event_detect(self._gpio.flow_sensor, GPIO.RISING, callback=self._flow_counter.flow_rate_callback, bouncetime=100)
      except RuntimeError as err:
        if re.match(err.__str__(), "Conflicting edge detection already enabled for this GPIO channel"):
          print "GPIO already configured elsewhere."
          self._gpio.cleanup()
        else:
          raise err

  def config():
      doc = "The config property."
      def fget(self):
          return self._config
      def fset(self, value):
          self._config = value
      def fdel(self):
          del self._config
      return locals()
  config = property(**config())

  def flow_reader():
      doc = "The flow_reader property."
      def fget(self):
          return self._flow_reader
      def fset(self, value):
          self._flow_reader = value
      def fdel(self):
          del self._flow_reader
      return locals()
  flow_reader = property(**flow_reader())

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

  def flow_switcher():
      doc = "The flow_switcher property."
      def fget(self):
          return self._flow_switcher
      def fset(self, value):
          self._flow_switcher = value
      def fdel(self):
          del self._flow_switcher
      return locals()
  flow_switcher = property(**flow_switcher()) 

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


  def start_readings_thread(self):
    Timer(self._config.reading_interval, self._flow_reader.take_reading, args=(self._flow_counter.give_reading(),)).start()

  def runner(self):
    try:
      while True:
        self.start_readings_thread()
        print "readings_set", self.flow_reader.readings_set
        current_ticks = self.readings_calculator.calculate_total(self.flow_reader.readings_set)
        current_gals = self.readings_calculator.to_gallons(current_ticks)
        print "Calculation: ", current_gals, "gallons"
        close_valve_query = self.flow_switcher.switch_flow_decider(current_gals)
        self.flow_switcher.switch_flow(close_valve_query, self.solenoid)
        time.sleep(5)
    except KeyboardInterrupt:
      print "kthxbai"
      sys.exit()
    finally:
      self._gpio.cleanup()

if __name__ == '__main__':
  Main().runner()
