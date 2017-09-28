import random
import click

word_list = "eff_large_wordlist.txt"
number_of_dice = 5 
#  number_of_words = 5

def create_word_list_dictionary(word_list):
  word_list_dict = {}
  with open(word_list) as file:
    for line in file:
      dice,word = line.split()
      word_list_dict[dice] = word
  return word_list_dict

#  Roll a number of dice one time
#  TODO: allow this function to be passed the random function that it uses, to integrate API
def roll_dice(number_of_dice):
  roll = ''
  for x in range(number_of_dice):
    roll += str(random.randint(1,6))
  return roll

def generate_diceware_password(numberOfWords, numberOfDice=number_of_dice, wordlist=word_list):
  password = ''
  words = create_word_list_dictionary(wordlist)
  for x in range(numberOfWords):
    password += words[roll_dice(numberOfDice)]
  return password

@click.command()
#  @click.option('--dice', default=5, help='The number of dice to be rolled')
@click.option('--words', default=5, help='The number of random words to generate')
def cli(words):
  """Generate a diceware password."""
  click.echo(generate_diceware_password(numberOfWords=words))
