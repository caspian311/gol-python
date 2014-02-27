import os
import sys

class Display:
   def show_board(self, data):
      os.system('clear')
      if len(data) > 0:
         sys.stdout.write(' ')
         for i in range(0, len(data[0])):
            sys.stdout.write('-')
      sys.stdout.write('\n')

      for x in range(0, len(data)):
         sys.stdout.write('|')
         for y in range(0, len(data[x])):
            sys.stdout.write(str(data[x][y]))
         sys.stdout.write('|')
         sys.stdout.write('\n')

      if len(data) > 0:
         sys.stdout.write(' ')
         for i in range(0, len(data[0])):
            sys.stdout.write('-')

      sys.stdout.write('\n')
