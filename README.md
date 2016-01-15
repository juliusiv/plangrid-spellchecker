# Plangrid Spellchecker

This is a REPL for spellchecking a string of text using multiple languages at a
time. This spellchecker is meant to be a toy simulation of Chrome's
multilanguage spellchecker. Currently, only English and Spanish are supported
but other languages can be added by adding a text file in the /languages
directory, named <language-name>.txt and where every line of the file is a
different word.

## Running
To run the spellchecker, just go to the root of the pg-spellchecker directory
and run python repl.py. You will be prompted to enter the languages you would
like to spellcheck with (separated by commas) and then you will enter the main
loop. If any of the languages you type in don't exist you will be asked to
re-enter the languages you'd like to spellcheck with.

When you enter the main loop you can:
- Type a sentence and the spellchecker will tell you which words are misspelled
  and give you suggestions for words you may have meant.
- Type "[add] <language-name>" to add the language <language-name> into the
  languages that you're currently using for spellchecking. If it doesn't exist,
  nothing will happen.
- Type "[remove] <language-name>" to remove the language <language-name> from
  the languages that you're currently using for spellchecking. If the language
  is currently being used then nothing will happen.
- Type "[exit]" and the program will end.