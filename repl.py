from spellchecker import Spellchecker


def loadDictionary(language):
  uri = "languages/" + language + ".txt"
  dictionary = set([])
  try:
    with open(uri) as f:
      dictionary = set((w.strip() for w in f))
    return dictionary
  except IOError:
    return None


def main():
  while True:
    language_inputs = raw_input("What languages would you like to use (ex. spanish,english)? ")
    language_list = (l.strip() for l in language_inputs.split(','))
    languages = {}
    for lang in language_list:
      dictionary = loadDictionary(lang)
      if dictionary is None:
        print "One of those dictionaries doesn't exist."
        continue
      else:
        languages[lang] = dictionary
    break
  # print languages

  spellchecker = Spellchecker(languages)

  while True:
    repl_input = raw_input("Enter a sentence or command => ")

    if repl_input.startswith("[exit]"):
      break

    elif repl_input.startswith("[remove]"):
      language = repl_input.split()[-1].lower()
      if spellchecker.removeLanguage(language):
        print "Successfully removed " + language
      else:
        print "Could not remove " + language

    elif repl_input.startswith("[add]"):
      language = repl_input.split()[-1].lower()
      dictionary = loadDictionary(language)
      if spellchecker.addLanguage(language, dictionary):
        print "Successfully added " + language
      else:
        print "Could not add " + language

    else:
      misspellings = spellchecker.check(repl_input)
      if len(misspellings) == 0:
        print "There are no misspellings!"
      else:
        print "\nMisspellings:"
        for m in misspellings:
          suggestions = spellchecker.suggest(m, 3)
          print "  {}: {}".format(m, ", ".join(suggestions))
        # printMisspellings(misspellings)

  # sample invocation:
  # print spellchecker.check("the Ball is bigg")
  # print spellchecker.check("hola, donde the... big ball")
  # print spellchecker.check("")

if __name__ == "__main__":
  main()
