from spellchecker import Spellchecker


def load_dictionary(language):
  uri = "languages/" + language + ".txt"
  dictionary = set([])
  try:
    with open(uri) as f:
      dictionary = set((w.strip() for w in f))
    return dictionary
  except IOError:
    return None


def handle_language_selection():
  language_inputs = raw_input("What languages would you like to use (ex. "
                              "spanish,english)? ")
  language_list = (l.strip() for l in language_inputs.split(','))
  languages = {}
  for lang in language_list:
    dictionary = load_dictionary(lang)
    if dictionary is None:
      return None
    else:
      languages[lang] = dictionary
  return languages


def handle_input(spellchecker, repl_input):
  output = None

  if repl_input.startswith("[exit]"):
    return None

  elif repl_input.startswith("[remove]"):
    language = repl_input.split()[-1].lower()
    if spellchecker.remove_language(language):
      output = "Successfully removed {}\n".format(language)
    else:
      output = "Could not remove {}\n".format(language)

  elif repl_input.startswith("[add]"):
    language = repl_input.split()[-1].lower()
    dictionary = load_dictionary(language)
    if spellchecker.add_language(language, dictionary):
      output = "Successfully added {}\n".format(language)
    else:
      output = "Could not add {}\n".format(language)

  else:
    misspellings = spellchecker.check(repl_input)
    if len(misspellings) == 0:
      output = "There are no misspellings!\n"
    else:
      output = "Misspellings:\n"
      for m in misspellings:
        suggestions = spellchecker.suggest(m, 3)
        output = "".join([output, "  {}: {}".format(m, ", ".join(suggestions))])
      output += '\n'
  return output


def main():
  languages = None
  while languages is None:
    languages = handle_language_selection()
    if languages is None:
      print "At least one of those dictionaries doesn't exist.\n"
  spellchecker = Spellchecker(languages)

  while True:
    repl_input = raw_input("Enter a sentence or command => ")
    output = handle_input(spellchecker, repl_input)
    if output is None:
      break
    print output
  print "Exiting the spellchecker"


if __name__ == "__main__":
  main()
