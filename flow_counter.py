class FlowCounter(int):
  def __init__(self):
    self._flow_ticks = 0

  # @property
  # def flow_ticks(self):
  #   # getter
  #   return self._flow_ticks

  # @flow_ticks.setter
  # def flow_ticks(self, value):
  #   # setter
  #   self._flow_ticks = value

  def flow_rate_callback(self):
    self._flow_ticks += 1
    # if args.debug >= 2:
    print "event was detected. flow_ticks: ", self._flow_ticks

  def give_reading(self):
    val = self._flow_ticks
    self._flow_ticks = 0
    return val

  def flow_ticks():
      doc = "The flow_ticks property."
      def fget(self):
          return self._flow_ticks
      def fset(self, value):
          self._flow_ticks = value
      def fdel(self):
          del self._flow_ticks
      return locals()
  flow_ticks = property(**flow_ticks())
