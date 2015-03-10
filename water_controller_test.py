import unittest
from water_controller import Main

class TestMain(unittest.TestCase):
  def setUp(self):
    self.a_main = Main()

  def test_threaded_readings(self):
    self.assertEqual(self.a_main.threaded_readings(), "0")

if __name__ == '__main__':
  unittest.main()