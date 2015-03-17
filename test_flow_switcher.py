from nose.tools import assert_equal
from flow_switcher import FlowSwitcher
from controller_config import ControllerConfig

class TestFlowSwitcher():
  def setUp(self):
    self.a_high_reading_total   = 2 #gallons
    self.a_low_reading_total    = 0.1
    self.a_config               = ControllerConfig()
    self.a_flow_switcher        = FlowSwitcher(self.a_config)
    self.mock_solenoid          = MockSolenoid()
    self.low_decision           = self.a_flow_switcher.switch_flow_decider(self.a_low_reading_total)
    self.high_decision          = self.a_flow_switcher.switch_flow_decider(self.a_high_reading_total)

  def test_switch_flow_decider(self):
    assert_equal(self.a_flow_switcher.switch_flow_decider(self.a_high_reading_total), True)
    assert_equal(self.a_flow_switcher.switch_flow_decider(self.a_low_reading_total), False)

  def test_switch_flow_low(self):
    low_result = self.a_flow_switcher.switch_flow(self.low_decision, self.mock_solenoid)
    assert_equal(self.mock_solenoid.sol_state, "open")

  def test_switch_flow_high(self):
    high_result = self.a_flow_switcher.switch_flow(self.high_decision, self.mock_solenoid)
    assert_equal(self.mock_solenoid.sol_state, "close")

  def test_switch_actuation_sets_Config_emergency_status(self):
    assert_equal(self.a_config.emergency_status, False)
    self.a_flow_switcher.switch_flow(self.high_decision, self.mock_solenoid)
    print "test flow switcher emergency status is : ", self.a_config.emergency_status
    assert_equal(self.a_config.emergency_status, True)

class MockSolenoid:
  def __init__(self):
    self._sol_state = None

  def sol_state():
      doc = "The sol_state property."
      def fget(self):
          return self._sol_state
      def fset(self, value):
          self._sol_state = value
      def fdel(self):
          del self._sol_state
      return locals()
  sol_state = property(**sol_state())

  def open(self):
    self.sol_state = "open"

  def close(self):
    self.sol_state = "close"