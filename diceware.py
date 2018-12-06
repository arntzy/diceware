#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import click

def create_word_list_dictionary(word_list):
  word_list_dict = {}
  word_list_lines = word_list.read().splitlines()
  for line in word_list_lines:
    dice,word = line.split()
    word_list_dict[dice] = word
  return word_list_dict

def roll_dice(number_of_dice):
  roll = ''
  for x in range(number_of_dice):
    roll += str(random.randint(1,6))
  return roll

def generate_diceware_password(numberOfWords, wordlist, numberOfDice):
  password = ''
  words = create_word_list_dictionary(wordlist)
  for x in range(numberOfWords):
    password += words[roll_dice(numberOfDice)]
  return password

# permutations 
def substitute_special_character(password):
    letter = random.choice(password)
    special_character = random.choice(['!','@','#','$','%','^','&','*'])
    new_password = password.replace(letter, special_character)
    return new_password

def substitute_number(password):
    letter = random.choice(password)
    number = random.choice(['0','1','2','3','4','5','6','7','8','9'])
    new_password = password.replace(letter, number)
    return new_password

def randomize_case(password, weight):
    new_password = ""
    for letter in password:
        if (random.random() <= weight):
            new_password += letter.upper()
        else:
            new_password += letter
    return new_password

@click.command()
@click.option('--dice', default=5, help='The number of dice to be rolled, default=5')
@click.option('--words', default=5, help='The number of random words to generate, default=5')
@click.option('--special_character', is_flag=True, help='Subsitute a special character for each instance of a letter')
@click.option('--number', is_flag=True, help='Substitute a random number for each instance of a letter')
@click.option('--random_case', is_flag=True, help='Change the case of letters randomly')
@click.argument('path_to_wordlist', type=click.File('r'))
def cli(words, path_to_wordlist, dice, random_case, special_character, number):
    """Generate a diceware password."""
    diceware_password = generate_diceware_password(numberOfWords=words, wordlist=path_to_wordlist, numberOfDice=dice)
    if random_case:
        weight = random.random()
        diceware_password = randomize_case(password=diceware_password, weight=weight)
    if number:
        diceware_password = substitute_number(password=diceware_password)
    if special_character:
        diceware_password = substitute_special_character(password=diceware_password)
    click.echo(diceware_password)
