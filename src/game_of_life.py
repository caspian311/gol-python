
from grid import Grid

class GameOfLife:
   def __init__(self, size):
      self._grid = Grid(size)

   def get_board(self):
      self._grid.update()
      return self._grid.get_data()


