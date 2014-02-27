import random

class Grid:
   MAX = 10
   def __init__(self):
      self._data = [[self._random_life() for x in range(Grid.MAX)] for x in range(Grid.MAX)]

   def _random_life(self):
      if random.choice([1, 2, 3, 5]) % 2 == 0:
         return '*'
      else:
         return ' '

   def update(self):
      pass

   def get_data(self):
      return self._data

