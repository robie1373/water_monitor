from flow_reader import FlowReader
from controller_config import ControllerConfig
from flow_counter import FlowCounter

class Main():
  def __init__(self):
    self._config          =ControllerConfig()
    self._flow_reader     = FlowReader(self._config)
    self._flow_counter    = FlowCounter()

  def flow_reader():
      doc = "The flow_reader property."
      def fget(self):
          return self._flow_reader
      def fset(self, value):
          self._flow_reader = value
      def fdel(self):
          del self._flow_reader
      return locals()
  flow_reader = property(**flow_reader())

  def flow_counter():
      doc = "The flow_counter property."
      def fget(self):
          return self._flow_counter
      def fset(self, value):
          self._flow_counter = value
      def fdel(self):
          del self._flow_counter
      return locals()
  flow_counter = property(**flow_counter())
