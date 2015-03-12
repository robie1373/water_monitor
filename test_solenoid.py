from nose.tools import assert_equal
from solenoid import Solenoid
import platform
import re

if re.match("arm", platform.machine()):
  # try:
  #   # import RPi.GPIO as GPIO
  # except RuntimeError:
  #   print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

  # from gpio_mgt import GPIOManagement
  # platform = "rpi"


  class TestSolenoid:
    def setUp(self):
      self.a_solenoid = Solenoid()

    def test_solenoid_can_open(self):
      assert_equal(self.a_solenoid.open(), "opened=True")

    def test_solenoid_can_close(self):
      assert_equal(self.a_solenoid.close(), "opened=False")