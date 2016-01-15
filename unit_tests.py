import unittest
from spellchecker import levDist, Spellchecker
from repl import loadDictionary

class SpellcheckerTests(unittest.TestCase):
  def testLoadDictionary(self):
    self.assertIsNotNone(loadDictionary("english"))
    self.assertIsNone(loadDictionary("englishhhh"))
    self.assertIsNotNone(loadDictionary("spanish"))

  def testLevDist(self):
    self.assertEqual(3, levDist("kitten", "sitting"))
    self.assertEqual(3, levDist("kitten", "sitting"))

  def testCheck(self):
    self.assertEqual(1, len(self.spellchecker.check("the Ball is bigg")))
    self.assertEqual(2, len(self.spellchecker.check("hola, donde the... big ball")))
    self.assertEqual(0, len(self.spellchecker.check("big ball")))

  def setUp(self):
    dictionaries = {"english": loadDictionary("english")}
    self.spellchecker = Spellchecker(dictionaries)

if __name__ == '__main__':
    unittest.main()
