class FlowCounter(int):
  def __init__(self):
    self._flow_ticks = 0

  def flow_rate_callback(self, args=None):
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
