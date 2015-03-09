class FlowReader():
  def __init__(self, config, starter_set=[0]):
    self._readings_set = starter_set
    self._config = config

  @property
  def readings_set(self):
    return self._readings_set

  def take_reading(self, flow_counter):
    if len(self._readings_set) >= int(
      self._config.moving_avg_interval / self._config.reading_interval):
      # drop first reading from array
      self._readings_set.pop(0)
    # add new reading to end of array
    self._readings_set.append(flow_counter.flow_ticks)
    flow_counter.flow_ticks = 0