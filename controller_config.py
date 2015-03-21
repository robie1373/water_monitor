class ControllerConfig():

  """Configuration settings for the flow_monitor instance. 
  Includes moving_avg_interval which is the window (in seconds) over which we want to average. defaults to 5 min
  Also reading_interval which is number of seconds to take between readings."""
  
  def __init__(self):
    self._moving_avg_interval   = 300 # seconds
    self._reading_interval      = 5 # seconds
    self._shutoff_value         = 1 # gallon
    self._emergency_status      = False

  def moving_avg_interval():
      doc = "The moving_avg_interval value."
      def fget(self):
          return self._moving_avg_interval
      def fset(self, value):
          self._moving_avg_interval = value
      def fdel(self):
          del self._moving_avg_interval
      return locals()
  moving_avg_interval = property(**moving_avg_interval()) 

  def reading_interval():
      doc = "The reading_interval property."
      def fget(self):
          return self._reading_interval
      def fset(self, value):
          self._reading_interval = value
      def fdel(self):
          del self._reading_interval
      return locals()
  reading_interval = property(**reading_interval()) 

  def shutoff_value():
      doc = "The shutoff_value property."
      def fget(self):
          return self._shutoff_value
      def fset(self, value):
          self._shutoff_value = value
      def fdel(self):
          del self._shutoff_value
      return locals()
  shutoff_value = property(**shutoff_value())

  def emergency_status():
      doc = "The emergency_status property."
      def fget(self):
          return self._emergency_status
      def fset(self, value):
          self._emergency_status = value
      def fdel(self):
          del self._emergency_status
      return locals()
  emergency_status = property(**emergency_status()) 
  
  def set_emergency_status(self, gpio, state):
    if state == True:
      self.emergency_status = True
      self.gpio.set_green_led("off")
      self.gpio.set_red_led("on")
    elif state == False:
      self.emergency_status = False
      self.gpio.set_green_led("on")
      self.gpio.set_red_led("off")
    else:
      raise ValueError("Emergency status must be True or False")
