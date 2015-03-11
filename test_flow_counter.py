import unittest
from nose.tools import assert_equal
from flow_counter import FlowCounter
  
class TestFlowCounter(unittest.TestCase):
  def setUp(self):
    self.a_flow_counter = FlowCounter()

  def test_Flow_Counter_Getter(self):
    self.assertEqual(self.a_flow_counter.flow_ticks, 0)

  def test_Flow_Counter_Setter(self):
    self.a_flow_counter.flow_ticks = 3
    self.assertEqual(self.a_flow_counter.flow_ticks, 3)

  def test_Flow_Counter_Adding(self):
    self.a_flow_counter.flow_ticks += 1
    self.assertEqual(self.a_flow_counter.flow_ticks, 1)

  def testF_low_Rate_Callback(self):
    self.a_flow_counter.flow_rate_callback()
    self.a_flow_counter.flow_rate_callback()
    self.assertEqual(self.a_flow_counter.flow_ticks, 2)

class TestFlowCounterWithNose:
  def setUp(self):
    self.a_flow_counter = FlowCounter()
    self.a_flow_counter.flow_ticks = 11

  def test_give_reading(self):
    assert_equal(self.a_flow_counter.give_reading(), 11)

  def test_give_reading_resets_flow_ticks(self):
    assert_equal(self.a_flow_counter.flow_ticks, 11)
    self.a_flow_counter.give_reading()
    assert_equal(self.a_flow_counter.flow_ticks, 0)

if __name__ == '__main__':
  unittest.main()