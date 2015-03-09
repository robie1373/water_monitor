import unittest
from controller_config import ControllerConfig

class TestControllerConfig(unittest.TestCase):
  def setUp(self):
    self.a_controller_config = ControllerConfig()

  def test_Config_includes_time_frame(self):
    self.assertEqual(self.a_controller_config.moving_avg_interval, 300)

  def test_config_includes_reading_interval(self):
    self.assertEqual(self.a_controller_config.reading_interval, 5)

  def test_can_change_time_frame(self):
    self.a_controller_config.moving_avg_interval = 10
    self.assertEqual(self.a_controller_config.moving_avg_interval, 10)

  def test_can_change_reading_interval(self):
    self.a_controller_config.reading_interval = 1
    self.assertEqual(self.a_controller_config.reading_interval, 1)

if __name__ == '__main__':
  unittest.main()