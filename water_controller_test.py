import unittest
from water_controller import FlowCounter

class Test(unittest.TestCase):
  def testFlowSensor(self):
    self.assertEqual(self.flow_sensor, 7)

if __name__ == '__main__':
  unittest.main()