from nose.tools import assert_equal
from controller_config import ControllerConfig

class TestControllerConfig():
  def setUp(self):
    self.a_controller_config = ControllerConfig()

  def test_Config_includes_time_frame(self):
    assert_equal(self.a_controller_config.moving_avg_interval, 300)

  def test_config_includes_reading_interval(self):
    assert_equal(self.a_controller_config.reading_interval, 5)

  def test_can_change_time_frame(self):
    self.a_controller_config.moving_avg_interval = 10
    assert_equal(self.a_controller_config.moving_avg_interval, 10)

  def test_can_change_reading_interval(self):
    self.a_controller_config.reading_interval = 1
    assert_equal(self.a_controller_config.reading_interval, 1)

  def test_config_includes_shutoff_value(self):
    assert_equal(self.a_controller_config.shutoff_value, 1)
