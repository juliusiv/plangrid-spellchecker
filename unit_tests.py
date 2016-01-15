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
    self.assertEqual(["bigg"],
                     self.spellchecker.check("the Ball is bigg"))
    self.assertEqual(["hola", "donde"],
                     self.spellchecker.check("hola, donde the... big ball"))
    self.assertEqual([], self.spellchecker.check("big ball"))
    self.assertEqual([], self.spellchecker.check(""))

    # Punctuation should have no effect on misspellings.
    self.assertEqual([], self.spellchecker.check("..,,,;;?,"))

    # Test some Spanish and English together.
    self.spellchecker.add_language("spanish", load_dictionary("spanish"))
    self.assertEqual(["bigg"], self.spellchecker.check("the Ball is bigg"))
    self.assertEqual([], self.spellchecker.check("hola, donde the... big ball"))
    self.assertEqual(["holla", "boyo"],
                     self.spellchecker.check("holla my boyo"))

  def test_add_language(self):
    span_dict = load_dictionary("spanish")
    self.assertTrue(self.spellchecker.add_language("spanish", span_dict))
    # English should already be in the spellchecker so it cannot be added.
    eng_dict = load_dictionary("english")
    self.assertFalse(self.spellchecker.add_language("english", eng_dict))

  def test_suggest(self):
    self.assertEqual(self._get_distances("bigg")[:3],
                     self.spellchecker.suggest("bigg", 3))
    self.assertEqual(self._get_distances("hola")[:3],
                     self.spellchecker.suggest("hola", 3))
    self.assertEqual(self._get_distances("boyo")[:3],
                     self.spellchecker.suggest("boyo", 3))
    self.assertEqual(self._get_distances("")[:3],
                     self.spellchecker.suggest("", 3))

  # Find the Levenshtein distance between |word| and every word in the current
  # spellchecking languages and return a sorted list of distance-word tuples.
  def _get_distances(self, word):
    distances = set([])
    languages = self.spellchecker.get_languages()
    for lang in languages:
      for w in languages[lang]:
        dist = lev_dist(word, w)
        distances.add((dist, w))
    return [d[1] for d in sorted(distances)]

  def setUp(self):
    dictionaries = {"english": load_dictionary("english")}
    self.spellchecker = Spellchecker(dictionaries)

if __name__ == '__main__':
    unittest.main()
