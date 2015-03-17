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
    self._state = None

  def open(self):
    GPIO.output(self._gpio_mgt.solenoid, self._gpio_mgt.relay_open)
    self._state = "opened=True"

  def close(self):
    GPIO.output(self._gpio_mgt.solenoid, self._gpio_mgt.relay_closed)
    self._state = "opened=False"

  def state():
      doc = "The state property."
      def fget(self):
          return self._state
      def fset(self, value):
          self._state = value
      def fdel(self):
          del self._state
      return locals()
  state = property(**state()) 
  