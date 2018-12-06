### About
- This is a diceware password generator. It will generate a secure, easy-for-humans-to-remember password like:
**unclogoverlayclimaticfogtimothy**

- Also with number, special character and case options to appease sites demanding such password features:
**u#cLogove4layCliMaticFogtimoThY**

- It uses a specific wordlist at the moment: `eff_large_wordlist.txt`
- To use a different wordlist, make sure it is formatted similarly to `eff_large_wordlist.txt`,
and that the `--dice` option matches the number of dice in the file.

### Requirements 
- Python 3.6
- The anaconda environment.yml has some packages with release numbers specific to Linux. Mac users can create a new python 3 virtual environment if desired.

### Installation
- (optional) Create and activate an anaconda virtual environment with `conda env create -f environment.yml`, or create a new virtual environment. 
- install the command line application with `pip install .`

### Use
- run `diceware --help` to see help docs
- example: `diceware eff_large_wordlist.txt --words=3 --special_character --number`

### Help

```
Usage: diceware [OPTIONS] PATH_TO_WORDLIST

  Generate a diceware password.

Options:
  --dice INTEGER       The number of dice to be rolled, default=5
  --words INTEGER      The number of random words to generate, default=5
  --special_character  Subsitute a special character for each instance of a
                       letter
  --number             Substitute a random number for each instance of a
                       letter
  --random_case        Change the case of letters randomly
  --help               Show this message and exit.
```
