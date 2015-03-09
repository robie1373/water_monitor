try:
  import RPi.GPIO as GPIO
except RuntimeError:
  print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BOARD)

## set up pins
# input pin for flow sensor

flow_sensor = 7
GPIO.setup(flow_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# input pin for manual override

override = 11
GPIO.setup(override, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# output pin for solenoid

solenoid = 12
GPIO.setup(solenoid, GPIO.OUT)

## use GPIO callback to detect water flow
def flow_rate_callback(flow_sensor):
  # put flow rate counter here

## calculate flowrate (if useful)

## calculate total flow over 5 minutes

## Home mode (do not turn off water)

## Away mode (turn off water if flow over 5 minutes exceeds threshold)

## Persist the data for logging

## Present the data and config for web interface

## Manual override (turn water on or off? with a switch)
