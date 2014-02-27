import sys
import time

from game_of_life import GameOfLife
from display import Display

class Main:
   def __init__(self, size):
      self._gol = GameOfLife(size)
      self._display = Display()

   def _do_cycle(self):
      self._display.show_board(self._gol.get_board())

   def start(self):
      while True:
         self._do_cycle()
         time.sleep(1)


if __name__ == "__main__":
   print 'recieved ' + str(sys.argv)
   if len(sys.argv) == 2:
      size = int(sys.argv[1])
   else:
      size = 10
   Main(size).start()
