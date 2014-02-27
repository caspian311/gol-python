import sys
import time

from game_of_life import GameOfLife
from display import Display

def run_game(size):
   gol = GameOfLife(size)
   display = Display()

   while True:
      display.show_board(gol.get_board())
      time.sleep(1)

if __name__ == "__main__":
   if len(sys.argv) == 2:
      size = int(sys.argv[1])
   else:
      size = 10
   run_game(size)
