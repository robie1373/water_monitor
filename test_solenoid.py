from nose.tools import assert_equal
from solenoid import Solenoid
import platform
import re

if re.match("arm", platform.machine()):

  class TestSolenoid:
    def setUp(self):
      self.a_solenoid = Solenoid()

    def test_solenoid_can_open(self):
      self.a_solenoid.open()
      assert_equal(self.a_solenoid.state, "opened=True")

    def test_solenoid_can_close(self):
      self.a_solenoid.close()
      assert_equal(self.a_solenoid.state, "opened=False")