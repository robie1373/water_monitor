try:
  import RPi.GPIO as GPIO
except RuntimeError:
  print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

from threading import Timer
import time

GPIO.setmode(GPIO.BOARD)

## set up pins
# input pin for flow sensor

flow_sensor = 7
GPIO.setup(flow_sensor, GPIO.IN)

## use GPIO callback to detect water flow
flow_ticks = 0
def print_callback(flow_sensor):
  global flow_ticks
  flow_ticks += 1
  print "An Event was detected!"
  print "flow_ticks: "
  print flow_ticks

GPIO.add_event_detect(flow_sensor, GPIO.RISING, callback=print_callback)

## calculate total flow over 5 minutes
### time frame for the moving average in seconds
moving_avg_time_frame = 300

### Interval to take measurements in seconds
reading_interval = 5
readings = []
