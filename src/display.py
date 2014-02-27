import sys

class Display:
   def show_board(self, data):
      if len(data) > 0:
         sys.stdout.write(' ')
         for i in range(0, len(data[0])):
            sys.stdout.write('-')
      sys.stdout.write('\n')

      for y in range(0, len(data)):
         sys.stdout.write('|')
         for x in range(0, len(data[y])):
            sys.stdout.write(str(data[x][y]))
         sys.stdout.write('|')
         sys.stdout.write('\n')

      if len(data) > 0:
         sys.stdout.write(' ')
         for i in range(0, len(data[0])):
            sys.stdout.write('-')

      sys.stdout.write('\n')
