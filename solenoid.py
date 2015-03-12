from gpio_mgt import GPIOManagement
import platform
import re

if re.match("arm", platform.machine()):
  try:
    import RPi.GPIO as GPIO
  except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")


class Solenoid():
  def __init__(self):
    self._gpio_mgt = GPIOManagement()

  def open(self):
    GPIO.output(self._gpio_mgt.solenoid, self._gpio_mgt.relay_open)
    return "opened=True"

  def close(self):
    GPIO.output(self._gpio_mgt.solenoid, self._gpio_mgt.relay_closed)