import unittest
from readings_calculator import ReadingsCalculator
  
class TestReadingsCalculator(unittest.TestCase):
  def setUp(self):
    self.a_reading_set = [1,1,2,3,5,8,13]
    self.a_readings_calculator = ReadingsCalculator()

  def test_calculator_averages_a_list_of_ints(self):
    self.assertEqual(self.a_readings_calculator.calculate_average(self.a_reading_set), int(4.7))



if __name__ == '__main__':
  unittest.main()