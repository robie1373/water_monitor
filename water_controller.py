import platform
import re

if re.match("arm", platform.machine()):
  try:
    import RPi.GPIO as GPIO
  except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

  from gpio_mgt import GPIOManagement
  platform = "rpi"

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
    _flow_counter = FlowCounter
    _flow_counter.flow_ticks = 0
    if platform == "rpi":
      _gpio = GPIOManagement()
      GPIO.add_event_detect(_gpio.flow_sensor, GPIO.RISING,
        callback=_flow_counter.flow_rate_callback, bouncetime=100)
    _x = 0
    _config = ControllerConfig()
    _flow_reader = FlowReader(_config)
    # _args = running_args


## calculate flowrate (if useful)


  def threaded_readings():
    Timer(_config.reading_interval,
     _flow_reader.take_reading(_flow_counter), ()).start()

# Main loop
  def run(self):
    while True:
      self.threaded_readings()

    #testing code
      # if _args.debug >=1:

      time.sleep(5)
      _x += 1
      print "Calculation #", _x, "\n", _flow_reader.readings_set, "\n",
      ReadingsCalculator(_flow_reader.readings_set).calculate_average()

if __name__ == '__main__':
  print "running Main().run"
  Main().run

## Home mode (do not turn off water)

## Away mode (turn off water if flow over 5 minutes exceeds threshold)

## Persist the data for logging

## Present the data and config for web interface

## Manual override (turn water on or off? with a switch)
