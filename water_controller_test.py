import unittest
import threading
import time
from water_controller import Main

class TestMain(unittest.TestCase):
  def setUp(self):
    self.a_main = Main()
    self.a_main.test_readings_set = [0]    

  def test_threaded_readings(self):
    self.assertEqual(threading.active_count(), 1)
    self.a_main.threaded_readings()
    self.assertEqual(threading.active_count(), 2)
    # time.sleep(7)
    # self.assertEqual(threading.active_count(), 1)

  def test_to_make_sure_FlowReader_take_reading_works_here(self):
    self.assertEqual(self.a_main.test_readings_set, [0])
    self.a_main.test_flow_reader.take_reading(self.a_main.test_flow_counter)
    self.assertEqual(self.a_main.test_readings_set, [0,1])

  # def test_threaded_readings_appends_readings_set(self):
  #   self.assertEqual(self.a_main.readings_set, [0])
  #   self.a_main.threaded_readings()
  #   time.sleep(7)
  #   self.assertEqual(self.a_main.readings_set, [0,1])


if __name__ == '__main__':
  unittest.main()