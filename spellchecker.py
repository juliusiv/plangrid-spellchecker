import re

class Spellchecker:
  def __init__(self, langs={}):
    self.languages = langs

  def check(self, text):
    words = normalize(text).split()
    misspelled = []

    for word in words:
      count = 0
      for language, dictionary in self.languages.iteritems():
        if word in dictionary:
          continue
        else:
          count += 1
      if count == len(self.languages):
        misspelled.append(word)
    return misspelled

  def addLanguage(self, lang, dictionary):
    if not lang in self.languages:
      self.languages[lang] = dictionary
      return True
    return False

  def removeLanguage(self, lang):
    if lang in self.languages:
      del self.languages[lang]
      return True
    return False

  def suggest(self, word, limit):
    # (edit_dist, suggestion)
    suggestions = []
    for lang in self.languages:
      for w in self.languages[lang]:
        # If |w| has a better edit distance than something in |suggestions| then
        # replace it.
        dist = levDist(word, w)
        if len(suggestions) < limit:
          suggestions.append((dist, w))
          suggestions.sort()
        elif dist < max(suggestions, key=lambda x: x[0]):
          suggestions.append((dist, w))
          suggestions.sort()
          suggestions.pop()
    return sorted((s[1] for s in suggestions))


def levDist(w1, w2):
  # print w1, w2
  if len(w1) == 0:
    return len(w2)
  if len(w2) == 0:
    return len(w1)

  if w1[-1] == w2[-1]:
    cost = 0
  else:
    cost = 1
  return min(levDist(w1, w2[:-1]) + 1, levDist(w1[:-1], w2) + 1,
             levDist(w1[:-1], w2[:-1]) + cost)


def normalize(sentence):
  return re.sub(r"[,.;<>/\"\[\]\{\}]", '', sentence.lower())
