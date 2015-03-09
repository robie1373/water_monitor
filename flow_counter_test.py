import unittest
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

if __name__ == '__main__':
  unittest.main()