class ControllerConfig():
  def __init__(self):
    self._moving_avg_interval = 300
    self._reading_interval = 5

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
