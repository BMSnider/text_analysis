import unittest
from text_analysis.input_filtering.src.input_filter import InputFilter

class TestGetWords(unittest.TestCase):
  def test_trailingPeriods(self):
    if1 = InputFilter('Simple string. Doesn\'t have punctuation, and stuff.')
    res1 = if1.get_words()
    self.assertEqual(res1, ['Simple', 'string', 'Doesn\'t', 'have', 'punctuation', 'and', 'stuff'])
  
  def test_miscPunctuation(self):
    if2 = InputFilter('Handles ellipsis..., lists: of, things, and semicolons; plus-dashes')
    res2 = if2.get_words()
    self.assertEqual(res2, ['Handles', 'ellipsis', 'lists', 'of', 'things', 'and', 'semicolons', 'plus-dashes'])

