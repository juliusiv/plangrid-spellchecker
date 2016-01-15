import re

class Spellchecker:
  def __init__(self, langs={}):
    self.languages = langs

  # Spellchecks a sequence of text |text| using all languages in the current
  # spellchecking dictionaries.
  def check(self, text):
    words = normalize(text).split()
    misspelled = []

    for word in words:
      if not self.is_spelled_correctly(word):
        misspelled.append(word)
    return misspelled

  # Spellchecks |word| against all current spellchecking dictionaries.
  def is_spelled_correctly(self, word):
    count = 0
    for language, dictionary in self.languages.iteritems():
      if word in dictionary:
        continue
      else:
        count += 1
    return count != len(self.languages)

  # Adds a language dictionary to the current spellchecking languages.
  def add_language(self, lang, dictionary):
    if lang not in self.languages:
      self.languages[lang] = dictionary
      return True
    return False

  # Removes a language dictionary from the current spellchecking languages.
  def remove_language(self, lang):
    if lang in self.languages:
      del self.languages[lang]
      return True
    return False

  # Suggests the closest |limit| number of words to |word| across all
  # spellchecking languages.
  def suggest(self, word, limit):
    suggestions = []
    for lang in self.languages:
      for w in self.languages[lang]:
        # If |w| has a better edit distance than something in |suggestions| then
        # replace it.
        dist = lev_dist(word, w)
        suggestions.append((dist, w))
        suggestions.sort()
        if len(suggestions) > limit:
          suggestions.pop()
    return (s[1] for s in sorted(suggestions))


# Finds the edit distance between two words.
def lev_dist(w1, w2):
  if len(w1) == 0:
    return len(w2)
  if len(w2) == 0:
    return len(w1)

  if w1[-1] == w2[-1]:
    cost = 0
  else:
    cost = 1
  return min(lev_dist(w1, w2[:-1]) + 1, lev_dist(w1[:-1], w2) + 1,
             lev_dist(w1[:-1], w2[:-1]) + cost)


# Removes punctuation and characters that aren't a part of words.
def normalize(sentence):
  return re.sub(r"[,.;?!<>/\"\[\]\{\}]", '', sentence.lower())
