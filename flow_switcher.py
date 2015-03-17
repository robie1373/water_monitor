class FlowSwitcher():
  def __init__(self, config):
    self._config = config

  def switch_flow_decider(self, readings_total):
    if readings_total > 1:
      return True
    else:
      return False

  def switch_flow(self, decision, solenoid):
    if decision == False:
      if not self._config.emergency_status: 
        solenoid.open()
      else:
        print """ 
        Emergency status is True. This means the emergency shutoff 
        has been activated. You should check for problems before 
        resetting this system to reopen the valve.
        """
    elif decision == True:
      solenoid.close()
      self._config.emergency_status = True
      print "emergency status set to: ", self._config.emergency_status
    else:
      raise ValueError("Solenoid must be True or False")