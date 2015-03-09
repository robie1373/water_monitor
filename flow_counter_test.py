import unittest
from flow_counter import FlowCounter
  
class Test(unittest.TestCase):
  def setUp(self):
    self.a_flow_counter = FlowCounter()

  def testFlowCounterGetter(self):
    self.assertEqual(self.a_flow_counter.flow_ticks, 0)

  def testFlowCounterSetter(self):
    self.a_flow_counter.flow_ticks = 3
    self.assertEqual(self.a_flow_counter.flow_ticks, 3)

  def testFlowCounterAdding(self):
    self.a_flow_counter.flow_ticks += 1
    self.assertEqual(self.a_flow_counter.flow_ticks, 1)

  def testFlowRateCallback(self):
    self.a_flow_counter.flow_rate_callback()
    self.a_flow_counter.flow_rate_callback()
    self.assertEqual(self.a_flow_counter.flow_ticks, 2)

if __name__ == '__main__':
  unittest.main()