class ReadingsCalculator:

  def __add(self,x,y):
    return x+y
    
  def calculate_average(self, readings_set):
    return reduce(self.__add, readings_set)/len(readings_set)
