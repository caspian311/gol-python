import random

class Grid:
   def __init__(self, size):
      self._size = size
      self._data = [[self._random_life() for x in range(self._size)] for x in range(self._size)]

   def _random_life(self):
      if random.choice([1, 2, 3, 5]) % 2 == 0:
         return '*'
      else:
         return ' '

   def update(self):
      new_data = [[' ' for x in range(self._size)] for x in range(self._size)]

      for x in range(0, len(new_data)):
         for y in range(0, len(new_data)):
            new_data[x][y] = '*' if self._should_live(x, y) else ' '

      self._data = new_data

   def _should_live(self, x, y):
      neighbors = self._number_of_neighbors(x, y) 
      if neighbors > 3 or neighbors < 2:
         return False
      return True

   def _number_of_neighbors(self, x, y):
      neighbors = 0
      if self._is_cell_alive(x - 1, y - 1):
         neighbors += 1
      if self._is_cell_alive(x - 1, y):
         neighbors += 1
      if self._is_cell_alive(x - 1, y + 1):
         neighbors += 1
      if self._is_cell_alive(x, y - 1):
         neighbors += 1
      if self._is_cell_alive(x, y + 1):
         neighbors += 1
      if self._is_cell_alive(x + 1, y - 1):
         neighbors += 1
      if self._is_cell_alive(x + 1, y):
         neighbors += 1
      if self._is_cell_alive(x + 1, y + 1):
         neighbors += 1
      return neighbors

   def _is_cell_alive(self, x, y):
      if x < 0 or x >= len(self._data):
         return False
      if y < 0 or y >= len(self._data[x]):
         return False
      return self._data[x][y] == '*'

   def get_data(self):
      return self._data

