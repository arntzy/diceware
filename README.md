### About
- This is a diceware password generator CLI.
- It uses a specific wordlist at the moment: eff_large_wordlist.txt
- To use a different wordlist, make sure it is formatted similarly to eff_large_wordlist.txt,
and that the `--dice` option matches the number of dice in the file.

## Requirements
- I use Anaconda for virtual enviroments.

### Installation
- create and activate a python virtual environment with `conda env create -f environment.yml`
- install the command line application with `pip install .`

### Use
- run `diceware --help` to see help docs
- example: `diceware eff_large_wordlist.txt --words=3 --special_character --number`

### Help

Usage: diceware [OPTIONS] WORDLIST

  Generate a diceware password.

Options:
  --dice INTEGER       The number of dice to be rolled
  --words INTEGER      The number of random words to generate
  --special_character  Subsitute a special character for each instance of a
                       letter
  --number             Substitute a random number for each instance of a
                       letter
  --random_case        Change the case of letters randomly
  --help               Show this message and exit.
