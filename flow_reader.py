class FlowReader():
  def __init__(self, config):
    self._readings_set = [0]
    self._config = config
    self._moving_avg_interval = config.moving_avg_interval
    self._reading_interval = config.reading_interval

  # @property
  # def readings_set(self):
  #   return self._readings_set

  def readings_set():
      doc = "The readings_set property."
      def fget(self):
          return self._readings_set
      def fset(self, value):
          self._readings_set = value
      def fdel(self):
          del self._readings_set
      return locals()
  readings_set = property(**readings_set())

  def take_reading(self, flow_reading):
    if len(self._readings_set) >= int(self._moving_avg_interval / self._reading_interval):
      # drop first reading from array
      self._readings_set.pop(0)
    # add new reading to end of array
    return self._readings_set.append(flow_reading)

