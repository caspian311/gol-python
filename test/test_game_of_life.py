import unittest

from game_of_life import GameOfLife

class TestGameOfLife(unittest.TestCase):

   def test_initialize_board_to_correct_size(self):
      test_object = GameOfLife(2)

      board = test_object.get_board()

      self.assertEqual(len(board), 2)
      self.assertEqual(len(board[0]), 2)
      self.assertEqual(len(board[1]), 2)

