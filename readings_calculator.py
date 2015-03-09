class ReadingsCalculator:
  def __init__(self, readings_set):
    self._readings_set = readings_set

  def __add(self,x,y):
    return x+y
    
  def calculate_average(self):
    return reduce(self.__add, self._readings_set)/len(self._readings_set)
