class FlowReader():
  def __init__(self, starter_set=[0]):
    self._readings_set = starter_set

  @property
  def readings_set(self):
    return self._readings_set

  def take_reading():

    global readings
    if len(readings) > int(moving_avg_time_frame / reading_interval):
      # drop first reading from array
      readings.pop(0)
    # add new reading to end of array
    readings.append(flow.flow_ticks)
    flow.flow_ticks = 0
    if args.debug >= 1:
      print "readings: ", readings, "flow_ticks: ", flow.flow_ticks

