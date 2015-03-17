class ReadingsCalculator:
  def __init__(self):
    self.__ticks_to_liter_constant = 7.5
    self.__ticks_to_total_time_const = 60 
    self.__liters_per_gallon = 3.79

  def __add(self,x,y):
    return x+y
    
  def calculate_average(self, readings_set):
    return reduce(self.__add, readings_set)/len(readings_set)

  def calculate_total(self, readings_set):
    return reduce(self.__add, readings_set)

  # def to_liters(self, readings_total):
  #   return readings_total / (self.__ticks_to_liter_constant * self.__ticks_to_total_time_const)

  def to_gallons(self, readings_total):
    return self.__liters_per_gallon * readings_total / (self.__ticks_to_liter_constant * self.__ticks_to_total_time_const) 