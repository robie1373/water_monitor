from nose.tools import assert_equal
from nose.tools import assert_almost_equals
from readings_calculator import ReadingsCalculator
  
class TestReadingsCalculator():
  def setUp(self):
    self.a_reading_set = [1,1,2,3,5,8,13]
    self.a_readings_calculator = ReadingsCalculator()

  def test_calculator_averages_a_list_of_ints(self):
    assert_equal(self.a_readings_calculator.calculate_average(self.a_reading_set), int(4.7))

  def test_calculate_total_from_list_of_ints(self):
    assert_equal(self.a_readings_calculator.calculate_total(self.a_reading_set), 33)


  """ 
  FlowSwitcher.switch_flow_decider() can't handle different units.
  At this point I'm just using gallons rather than fix that.
  """
  # def test_to_liters(self):
  #   a = 10
  #   assert_equal(self.a_readings_calculator.to_liters(a), a * 7.5 * 60)

  def test_to_gallons(self):
    a = 13
    ticks_to_liter_constant = 7.5
    seconds = 60
    liters_per_gallon = 3.79
    assert_almost_equals(self.a_readings_calculator.to_gallons(a), a / (ticks_to_liter_constant * seconds) * liters_per_gallon)
