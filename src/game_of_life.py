from display import Display
from grid import Grid

class GameOfLife:
   def __init__(self):
      self._display = Display()
      self._grid = Grid()

   def _do_cycle(self):
      self._grid.update()
      self._display.show_board(self._grid.get_data())

   def start(self):
      for x in range(0, 10):
         self._do_cycle()

