try:
  import RPi.GPIO as GPIO
except RuntimeError:
  print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

from threading import Timer
import time
import argparse

from flow_counter import FlowCounter
from controller_config import ControllerConfig
from flow_reader import FlowReader
from readings_calculator import ReadingsCalculator
parser = argparse.ArgumentParser(description="Start and control water monitor system")

parser.add_argument('-d', '--debug', type=int, choices=[0,1,2],
 help="0 - no debug (default), 1 - print activity, 2 - print sensor events and activity",
 default=0)

args = parser.parse_args()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
## set up pins
# input pin for flow sensor

flow_sensor = 7
GPIO.setup(flow_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# input pin for manual override

override = 11
GPIO.setup(override, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# output pin for solenoid

solenoid = 16
GPIO.setup(solenoid, GPIO.OUT)

## use GPIO callback to detect water flow

# class FlowCounter(int):
#   def __init__(self):
#     self.flow_ticks = 0

#   @property
#   def flow_ticks(self):
#     # getter
#     return self._flow_ticks

#   @flow_ticks.setter
#   def flow_ticks(self, value):
#     # setter
#     self.flow_ticks = value

flow_counter = FlowCounter
flow_counter.flow_ticks = 0
# def flow_rate_callback(flow_sensor):
#   flow.flow_ticks += 1
#   if args.debug >= 2:
#     print "event was detected. flow.flow_ticks: ", flow.flow_ticks

GPIO.add_event_detect(flow_sensor, GPIO.RISING, callback=flow_counter.flow_rate_callback, bouncetime=100)

## calculate flowrate (if useful)

## calculate total flow over 5 minutes
### time frame for the moving average in seconds
# moving_avg_time_frame = 10

### Interval to take measurements in seconds
# reading_interval = 1
# readings = [0]

# def take_reading():
#   if args.debug >=1:
#     print "taking a reading"

#   global readings
#   if len(readings) > int(moving_avg_time_frame / reading_interval):
#     # drop first reading from array
#     readings.pop(0)
#   # add new reading to end of array
#   readings.append(flow.flow_ticks)
#   flow.flow_ticks = 0
#   if args.debug >= 1:
#     print "readings: ", readings, "flow_ticks: ", flow.flow_ticks

x = 0
config = ControllerConfig()
flow_reader = FlowReader(config)

def threaded_readings(interval, flow_reader):
  Timer(interval, flow_reader.take_reading(flow_counter), ()).start()

# def add(x,y):
#   return x+y
  
# def calculate_average():
#   return reduce(add, readings)/len(readings)

## Home mode (do not turn off water)

## Away mode (turn off water if flow over 5 minutes exceeds threshold)

## Persist the data for logging

## Present the data and config for web interface

## Manual override (turn water on or off? with a switch)

# Main loop

while True:
  threaded_readings(config.reading_interval(), flow_reader)

#testing code
  if args.debug >=1:
    print "Calculation #", x
    print flow_reader.readings_set
    print ReadingsCalculator(flow_reader.readings_set).calculate_average()

  time.sleep(5)
  x += 1