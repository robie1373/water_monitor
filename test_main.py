from nose.tools import assert_equal
from nose.tools import timed
from main import Main
import time

class TestMain:
  def setUp(self):
    self.a_main = Main()

  def test_main_has_flow_reader(self):
    assert self.a_main.flow_reader.readings_set

  def test_main_has_tick_counter(self):
    assert_equal(self.a_main.flow_counter.flow_ticks, 0)

  def test_main_can_update_readings_set_with_flow_ticks(self):
    assert_equal(self.a_main.flow_reader.readings_set, [0])
    self.a_main.flow_reader.take_reading(self.a_main.flow_counter.flow_ticks)
    assert_equal(self.a_main.flow_reader.readings_set, [0,0])

  @timed(0.7)
  def test_main_updates_reading_set_in_timed_thread(self):
    self.a_main.config.reading_interval = 0.5
    assert_equal(self.a_main.flow_reader.readings_set, [0])
    self.a_main.flow_counter.flow_ticks = 8
    self.a_main.threaded_readings()
    time.sleep(0.6)
    assert_equal(self.a_main.flow_reader.readings_set, [0,8])

  def test_main_averages(self):
    assert_equal(self.a_main.readings_calculator.calculate_average([8,4,6]), 6)

  def test_main_take_readings(self):
    self.a_main._flow_counter.flow_ticks = 4
    self.a_main.main_take_reading(self.a_main._flow_counter.flow_ticks)
    assert_equal(self.a_main.flow_reader.readings_set, [0,4])
    assert_equal(self.a_main._flow_counter.flow_ticks, 0)