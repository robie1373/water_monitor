import platform
import re

if re.match("arm", platform.machine()):
  try:
    import RPi.GPIO as GPIO
  except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

  from gpio_mgt import GPIOManagement
  platform = "rpi"
  print "I am running on an rpi"

from threading import Timer
import time

from flow_counter import FlowCounter
from controller_config import ControllerConfig
from flow_reader import FlowReader
from readings_calculator import ReadingsCalculator



# set up code

class Main():

  """ setup and run main body code """

  # def __init__(self, running_args):
  def __init__(self):
    self._flow_counter            = FlowCounter()
    self._flow_counter.flow_ticks = 0

    if platform == "rpi":
      self._gpio                  = GPIOManagement()
      try:
        GPIO.add_event_detect(self._gpio.flow_sensor, GPIO.RISING, callback=self._flow_counter.flow_rate_callback, bouncetime=100)
      except RuntimeError as err:
        if re.match(err.__str__(), "Conflicting edge detection already enabled for this GPIO channel"):
          print "GPIO already configured elsewhere."
          self._gpio.cleanup()
        else:
          raise err

    self._x                       = 0
    self._config                  = ControllerConfig()
    self._flow_reader             = FlowReader(self._config)
    # _args                        = running_args

  #########
  #
  # testing zone. Do not use these for anything but unittesting. They are all
  # available from the various classes in which they belong. You have been
  # warned.
  #
  ########

  def test_config():
      doc = "The test_config do not use."
      def fget(self):
          return self._config
      def fset(self, value):
          self._config = value
      return locals()
  test_config = property(**test_config())

  def test_flow_counter():
      doc = "The test_flow_counter. do not use."
      def fget(self):
          return self._flow_counter
      return locals()
  test_flow_counter = property(**test_flow_counter())

  def test_flow_reader():
      doc = "The test_flow_reader do not use."
      def fget(self):
          return self._flow_reader
      return locals()
  test_flow_reader = property(**test_flow_reader())

  def test_readings_set():
      doc = "a readings_set for testing purposes only. Do not use this. Use the one in FlowReader"
      def fget(self):
          return self._flow_reader.readings_set
      def fset(self, value):
          self._flow_reader.readings_set = value
      return locals()
  test_readings_set = property(**test_readings_set())

  def main_take_reading(self, val):
    self._flow_reader.take_reading(val)

  ##########
  #
  # end of testing zone. Your regular service is resumed
  #
  ##########

  def threaded_readings(self):
    print "i am threaded readings"
    take_reading = self._flow_reader.take_reading(self._flow_counter)
    print "take_reading: ", take_reading
    Timer(self._config.reading_interval,
     take_reading, ()).start()

  # Main loop
  def runner(self):
    try:
      print "this is the head of main().run"
      while True:
        print "I am true"
        self.threaded_readings()
        print "thread ran"
        time.sleep(5)
        print "I slept"
        self._x += 1
        print "Calculation #", self._x, "\n", self._flow_reader.readings_set, "\n",
        ReadingsCalculator(self._flow_reader.readings_set).calculate_average()
        print "ran the calculation"
    finally:
      self._gpio.cleanup()

if __name__ == '__main__':
  print "running Main().run"
  Main().run

## Home mode (do not turn off water)

## Away mode (turn off water if flow over 5 minutes exceeds threshold)

## Persist the data for logging

## Present the data and config for web interface

## Manual override (turn water on or off? with a switch)
