from nose.tools import assert_equal
from main import Main

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