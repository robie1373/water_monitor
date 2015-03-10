import unittest
from flow_reader import FlowReader
from flow_counter import FlowCounter
from controller_config import ControllerConfig

class TestFlowReader(unittest.TestCase):
  def setUp(self):
    self.a_flow_counter                           = FlowCounter()
    self.a_flow_counter.flow_ticks                = 5
    self.a_controller_config                      = ControllerConfig()
    self.a_controller_config.moving_avg_interval  = 4
    self.a_controller_config.reading_interval     = 1
    self.a_flow_reader            = FlowReader(self.a_controller_config)

  def test_Readings_Set_Init(self):
    self.assertEqual(self.a_flow_reader.test_readings_set, [0])

  def test_Take_readings_adds_an_element(self):
    self.a_flow_reader.take_reading(self.a_flow_counter)
    self.assertEqual(self.a_flow_reader.test_readings_set, [0,5])

  def test_take_readings_limits_len_to_timeframe_over_interval(self):
    for _ in range(5):
      self.a_flow_counter.flow_ticks = _
      self.a_flow_reader.take_reading(self.a_flow_counter)

    self.assertEqual(len(self.a_flow_reader.test_readings_set), 
      int(self.a_controller_config.moving_avg_interval / self.a_controller_config.reading_interval) )

  def test_take_readings_resets_ticks_to_zero(self):
    self.assertEqual(self.a_flow_counter.flow_ticks, 5)
    self.a_flow_counter.flow_ticks = 22
    self.a_flow_reader.take_reading(self.a_flow_counter)
    self.assertEqual(self.a_flow_counter.flow_ticks, 0)


class TestFlowReaderWithDefaultSettings(unittest.TestCase):
  def setUp(self):
    self.a_flow_counter             = FlowCounter()
    self.a_flow_counter.flow_ticks  = 5
    self.a_controller_config        = ControllerConfig()
    self.a_flow_reader              = FlowReader(self.a_controller_config)

  def test_take_readings_limits_len_to_timeframe_over_interval(self):
    for _ in range(300):
      self.a_flow_counter.flow_ticks = _
      self.a_flow_reader.take_reading(self.a_flow_counter)

    self.assertEqual(len(self.a_flow_reader.test_readings_set), 
      int(self.a_controller_config.moving_avg_interval / self.a_controller_config.reading_interval) )


if __name__ == '__main__':
  unittest.main()