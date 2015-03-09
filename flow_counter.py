class FlowCounter(int):
  def __init__(self, value=0):
    self.flow_ticks = value

  @property
  def flow_ticks(self):
    # getter
    return self._flow_ticks

  @flow_ticks.setter
  def flow_ticks(self, value):
    # setter
    self._flow_ticks = value

  def flow_rate_callback(self):
    self._flow_ticks += 1
    # if args.debug >= 2:
    #   print "event was detected. flow_ticks: ", self._flow_ticks
