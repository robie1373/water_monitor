import unittest
from flow_reader import FlowReader
# from flow_counter import FlowCounter
from controller_config import ControllerConfig
from nose.tools import assert_equals
from nose.tools import with_setup

class TestFlowReader(unittest.TestCase):
  def setUp(self):
    # self.a_flow_counter                           = FlowCounter()
    self.a_controller_config                      = ControllerConfig()
    self.a_flow_counter                           = self.a_controller_config.flow_counter
    self.a_flow_counter.flow_ticks                = 5
    self.a_controller_config.moving_avg_interval  = 4
    self.a_controller_config.reading_interval     = 1
    self.a_flow_reader                    = FlowReader(self.a_controller_config)


  def test_take_readings_limits_len_to_timeframe_over_interval(self):
    for _ in range(5):
      self.a_flow_counter.flow_ticks = _
      self.a_flow_reader.take_reading(self.a_flow_counter.give_reading())

    self.assertEqual(len(self.a_flow_reader.readings_set), 
      int(self.a_controller_config.moving_avg_interval / self.a_controller_config.reading_interval) )

  def test_take_readings_resets_ticks_to_zero(self):
    self.assertEqual(self.a_flow_counter.flow_ticks, 5)
    self.a_flow_counter.flow_ticks = 22
    self.a_flow_reader.take_reading(self.a_flow_counter.give_reading())
    self.assertEqual(self.a_flow_counter.flow_ticks, 0)


class TestFlowReaderWithDefaultSettings(unittest.TestCase):
  def setUp(self):
    self.a_controller_config        = ControllerConfig()
    self.a_flow_counter             = self.a_controller_config.flow_counter
    self.a_flow_counter.flow_ticks  = 5
    self.a_flow_reader              = FlowReader(self.a_controller_config)

  def test_take_readings_limits_len_to_timeframe_over_interval(self):
    for _ in range(300):
      self.a_flow_counter.flow_ticks = _
      self.a_flow_reader.take_reading(self.a_flow_counter.give_reading())

    self.assertEqual(len(self.a_flow_reader.readings_set), 
      int(self.a_controller_config.moving_avg_interval / self.a_controller_config.reading_interval) )

class TestFlowReaderNose:
  def setUp(self):
    self.a_controller_config                      = ControllerConfig()
    self.a_flow_counter                           = self.a_controller_config.flow_counter
    self.a_flow_counter.flow_ticks                = 5
    self.a_controller_config.moving_avg_interval  = 4
    self.a_controller_config.reading_interval     = 1
    self.a_flow_reader            = FlowReader(self.a_controller_config)

  def test_Readings_Set_Init(self):
    another_controller_config = ControllerConfig()
    another_flow_reader = FlowReader(another_controller_config)
    assert_equals(another_flow_reader.readings_set, [0])

  def test_Take_readings_adds_an_element(self):
    self.a_flow_reader.take_reading(self.a_flow_counter.give_reading())
    assert_equals(self.a_flow_reader.readings_set, [0,5])

if __name__ == '__main__':
  unittest.main()