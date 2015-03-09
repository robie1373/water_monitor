class ControllerConfig():
  def __init__(self):
    self._moving_avg_interval = 300
    self._reading_interval = 5

  def moving_avg_interval(self):
    return self._moving_avg_interval

  def reading_interval(self):
    return self._reading_interval