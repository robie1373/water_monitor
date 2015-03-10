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
import argparse

from flow_counter import FlowCounter
from controller_config import ControllerConfig
from flow_reader import FlowReader
from readings_calculator import ReadingsCalculator

# parser = argparse.ArgumentParser(description="Start and control water monitor system")

# parser.add_argument('-d', '--debug', type=int, choices=[0,1,2],
#  help="0 - no debug (default), 1 - print activity, 2 - print sensor events and activity",
#  default=0)

# args = parser.parse_args()


# set up code

class Main():

  """ setup and run main body code """

  # def __init__(self, running_args):
  def __init__(self):
    self._flow_counter            = FlowCounter
    self._flow_counter.flow_ticks = 0
    
    if platform == "rpi":
      self._gpio                  = GPIOManagement()
      GPIO.add_event_detect(self._gpio.flow_sensor, GPIO.RISING,
        callback=self._flow_counter.flow_rate_callback, bouncetime=100)

    self._x                       = 0
    self._config                  = ControllerConfig()
    self._flow_reader             = FlowReader(self._config)
    # _args                        = running_args

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

  def readings_set():
      doc = "a readings_set for testing purposes only. Do not use this. Use the one in FlowReader"
      def fget(self):
          return self._flow_reader.readings_set
      def fset(self, value):
          self._flow_reader.readings_set = value
      return locals()
  readings_set = property(**readings_set())

  def threaded_readings(self):
    print "i am threaded readings"
    take_reading = self._flow_reader.take_reading(self._flow_counter)
    print "take_reading: ", take_reading
    Timer(self._config.reading_interval,
     take_reading, ()).start()

# Main loop
  def run(self):
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

if __name__ == '__main__':
  print "running Main().run"
  Main().run

## Home mode (do not turn off water)

## Away mode (turn off water if flow over 5 minutes exceeds threshold)

## Persist the data for logging

## Present the data and config for web interface

## Manual override (turn water on or off? with a switch)
