try:
  import RPi.GPIO as GPIO
except RuntimeError:
  print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

from threading import Timer
import time
import arguments


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
flow_ticks = 0
def flow_rate_callback(flow_sensor):
  global flow_ticks
  flow_ticks += 1
  if args.debug >= 2:
    print "event was detected. flow_ticks: ", flow_ticks

GPIO.add_event_detect(flow_sensor, GPIO.RISING, callback=flow_rate_callback, bouncetime=100)

## calculate flowrate (if useful)

## calculate total flow over 5 minutes
### time frame for the moving average in seconds
moving_avg_time_frame = 10

### Interval to take measurements in seconds
reading_interval = 1
readings = [0]

def take_reading():
  if args.debug >=1:
    print "taking a reading"

  global flow_ticks
  global readings
  if len(readings) > int(moving_avg_time_frame / reading_interval):
    # drop first reading from array
    readings.pop(0)
  # add new reading to end of array
  readings.append(flow_ticks)
  flow_ticks = 0
  if args.debug >= 1:
    print "readings: ", readings, "flow_ticks: ", flow_ticks

def threaded_readings(interval):
  Timer(interval, take_reading, ()).start()

def add(x,y):
  return x+y
  
def calculate_average():
  if args.debug >= 1:
    print "calculating the average of ", readings

  return reduce(add, readings)/len(readings)

## Home mode (do not turn off water)

## Away mode (turn off water if flow over 5 minutes exceeds threshold)

## Persist the data for logging

## Present the data and config for web interface

## Manual override (turn water on or off? with a switch)

# Main loop
x = 0
while True:
  threaded_readings(reading_interval)

#testing code
  if args.debug >=1:
    print "Calculation #", x
    print readings
    print calculate_average()
    
  time.sleep(5)
  x += 1