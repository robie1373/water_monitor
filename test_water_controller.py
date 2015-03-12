# import threading
# import time
# from nose.tools import assert_equal
# from water_controller import Main

# class TestMain():
#   def setUp(self):
#     self.a_main = Main()

#   # def test_threaded_readings(self):
#   #   assert_equal(threading.active_count(), 1)
#   #   self.a_main.threaded_readings()
#   #   assert_equal(threading.active_count(), 2)
    
#   def test_what_config_looks_like_right_now(self):
#     assert_equal(self.a_main.test_config.moving_avg_interval, 300)
#     assert_equal(self.a_main.test_config.reading_interval, 5)

# class TestMainTakeReading:
#   def setUp(self):
#     self.a_main = Main()
#     self.a_main.test_flow_reader.readings_set = [0,43,11]    
    
#   def test_flow_reader_looks_sane(self):
#     assert dir(self.a_main.test_flow_reader).__contains__("take_reading")

#   def test_to_make_sure_FlowReader_take_reading_works_here(self):
#     orig_len = len(self.a_main.test_flow_reader.readings_set)
#     print "\norig readings set: ", self.a_main.test_flow_reader.readings_set

#     self.a_main.main_take_reading(96)

#     new_len = len(self.a_main.test_flow_reader.readings_set)
#     print "new readings set: ", self.a_main.test_flow_reader.readings_set
    
#     assert_equal(new_len, orig_len + 1)
    
#   # def test_threaded_readings_appends_readings_set(self):
#   #   assert_equal(self.a_main.readings_set, [0])
#   #   self.a_main.threaded_readings()
#   #   time.sleep(7)
#   #   assert_equal(self.a_main.readings_set, [0,1])


# if __name__ == '__main__':
#   unittest.main()