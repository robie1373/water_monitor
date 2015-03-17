from controller_config import ControllerConfig

class FlowSwitcher():
  def __init__(self):
    self._config = ControllerConfig()

  def switch_flow_decider(self, readings_total):
    if readings_total > 1:
      return True
    else:
      return False

  def switch_flow(self, decision, solenoid):
    if decision == True:
      solenoid.open()
    elif decision == False:
      solenoid.close()
    else:
      raise ValueError("Solenoid must be True or False")