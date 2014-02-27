import sys
from game_of_life import GameOfLife

if __name__ == "__main__":
   print 'recieved ' + str(sys.argv)
   if len(sys.argv) == 3:
      size = int(sys.argv[1])
      cycles = int(sys.argv[2])
   else:
      size = 10
      cycles = 100
   GameOfLife(size, cycles).start()
