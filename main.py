import platform
import re
from flow_reader import FlowReader
from controller_config import ControllerConfig
from flow_counter import FlowCounter
from threading import Timer
from readings_calculator import ReadingsCalculator

class Main():
  def __init__(self):
    self._config          =ControllerConfig()
    self._flow_reader     = FlowReader(self._config)
    self._flow_counter    = FlowCounter()
    self._readings_calculator = ReadingsCalculator()

    if platform == "rpi":
      self._gpio                  = GPIOManagement()
      print "I am an RPi"
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

  def threaded_readings(self):
    Timer(self._config.reading_interval, self._flow_reader.take_reading, args=(self._flow_counter.flow_ticks,)).start()

  def runner(self):
    try:
      while True:
        self.threaded_readings()
        print "Calculation: ", self.readings_calculator.calculate_average(self.flow_reader.readings_set)
    finally:
      self._gpio.cleanup()

if __name__ == '__main__':
  Main().runner()
