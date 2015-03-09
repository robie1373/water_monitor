import unittest
from flow_reader import FlowReader
  
class Test(unittest.TestCase):
  def setUp(self):
    self.a_flow_reader = FlowReader()

  def testReadinsSetInit(self):
    self.assertEqual(self.a_flow_reader.readings_set, [0])

if __name__ == '__main__':
  unittest.main()