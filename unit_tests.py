import unittest
from spellchecker import lev_dist, Spellchecker
from repl import load_dictionary

class SpellcheckerTests(unittest.TestCase):
  def test_load_dictionary(self):
    self.assertIsNotNone(load_dictionary("english"))
    self.assertIsNone(load_dictionary("englishhhh"))
    self.assertIsNotNone(load_dictionary("spanish"))

  def test_lev_dist(self):
    self.assertEqual(3, lev_dist("kitten", "sitting"))
    self.assertEqual(3, lev_dist("saturday", "sunday"))    
    self.assertEqual(1, lev_dist("can", "pan"))
    self.assertEqual(0, lev_dist("rosebud", "rosebud"))

  def test_check(self):
    # Test only English words.
    self.assertEqual(1, len(self.spellchecker.check("the Ball is bigg")))
    self.assertEqual(2, len(self.spellchecker.check("hola, donde the... big "
                                                    "ball")))
    self.assertEqual(0, len(self.spellchecker.check("big ball")))
    self.assertEqual(0, len(self.spellchecker.check("")))
    # Punctuation should have no effect on misspellings.
    self.assertEqual(0, len(self.spellchecker.check("..,,,;;?,")))

    # Test some Spanish and English together.
    self.spellchecker.add_language("spanish", load_dictionary("spanish"))
    self.assertEqual(1, len(self.spellchecker.check("the Ball is bigg")))
    self.assertEqual(0, len(self.spellchecker.check("hola, donde the... big "
                                                    "ball")))
    self.assertEqual(2, len(self.spellchecker.check("holla my boyo")))

  def test_add_language(self):
    span_dict = load_dictionary("spanish")
    self.assertTrue(self.spellchecker.add_language("spanish", span_dict))
    # English should already be in the spellchecker so it cannot be added.
    eng_dict = load_dictionary("english")
    self.assertFalse(self.spellchecker.add_language("english", eng_dict))

  def setUp(self):
    dictionaries = {"english": load_dictionary("english")}
    self.spellchecker = Spellchecker(dictionaries)

if __name__ == '__main__':
    unittest.main()
