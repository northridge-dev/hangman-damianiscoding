# BANNER and HANGMAN_PICS are some ASCII art
# Create your own ASCII art if you desire, but
# ONLY AFTER getting the game logic working.
from ascii_art import BANNER, HANGMAN_PICS

# uncomment the import statement, below, when
# you're ready to implement a one player version
# of the game.
# `animal_words` is a list of . . . animal words.
# Feel free to add more words or word categories.
# from word_lists import animal_words

"""
Here's where you'll write your code. 
  - Follow the instructions in the README file.
  - If you try to write all the code in `play_hangman`, 
    it's going to be a mess. Instead, break your logic
    into smaller functions that you can call from 
    `play_hangman`.

Run your code from the terminal:
  - make sure you're in the right directory (`projects/hangman`)
    - if you're not sure how to get to the right directory, ask!
  - make sure you're at the command line prompt, not in the Python shell (not >>>)
  - type the following command: python hangman.py

Tests? No tests for this project. 
"""
from random import randint
import os
os.system('clear')

# `play_hangman` is the main function, the function
# that will orchestrate all the helper functions
# you define, above.
def play_hangman():
  # rules
  print(BANNER)
  print("""This is the Hangman Game!
  There are 2 players involved in the game.
  Player 1 will be making a 4 to 24 letter word.
  The word could only have lowercase letters.")
  Player 2 will then try to guess letters in that word.
  player 2 can only guess one letter at a time.
  Player 2 has 6 lives before he loses.""")
  start = input("Type 's' when you want to start. ")

  # Game starts
  if start == 's': 
    the_word = input("Player 1, what is your word? ")
    len_of_word = len(the_word)
    word_check_list = word_check(the_word, len_of_word)
    the_word = word_check_list[0]
    len_of_word = word_check_list[1]
    os.system('clear')

    # variables
    attempts = 1
    correct_guess = 0
    previous_correct_guess = 0
    lives = 6
    round = 0
    # the 'used' variables are for keeping track what letter has already been used
    guessed_letters = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #print how many letters are in the word
    the_word_list = []
    for i in range(len_of_word):
      the_word_list.append('_')

    #print screen
    print(HANGMAN_PICS[0])
    print(the_word_list)

    # player 2 guesses
    while lives > 0:
      guess = input("Player 2, what letter do you guess? ")
      guess = letter_check(guess, guessed_letters)

      guessed_letters[round - 1] = guess
      place = 0
      correct_for_round = 0
      round += 1
      os.system('clear')

      #check to see whether letter is correct
      for letter in range(len_of_word):
        if guess == the_word[place]:
          correct_guess += 1
          correct_for_round += 1
          place += 1
          the_word_list[place - 1] = guess
        else:
          place += 1
      if correct_guess != previous_correct_guess:
        print("There is a:" ,guess)
        previous_correct_guess += correct_for_round
      else:
        lives -= 1
        print("That is not the letter.")
      
      #check if the player won yet
      if correct_guess == len_of_word:
        print('YOU WIN!!!')
        break

      #show how many lives are left
      life_system(lives)
      if lives == 0:
        print(HANGMAN_PICS[6])
        print("You Lose")
        print("The word was", the_word)
      print(the_word_list)


# Here's where you can define helper functions

#checks whether player 1 word is valid
def word_check(the_word, len_of_word):
  while True:
    # checking length of word 
    if len_of_word < 4:
      os.system('clear')
      print("That word is too short.")
      the_word = input("Player 1, what is your word? ")
      len_of_word = len(the_word)
    elif len_of_word > 24:
      os.system('clear')
      print("That word is too long.")
      the_word = input("Player 1, what is your word? ")
      len_of_word = len(the_word)
    # checking if it is a lower case letter
    else:
      place = 0
      counter = 0
      for lowercase in range(len_of_word):
        if ord(the_word[place]) < 97 or ord(the_word[place]) > 122:
          os.system('clear')
          print("The word can only have lowercase letters.")
          the_word = input("Player 1, what is your word? ")
          len_of_word = len(the_word)
          counter = -1
          break
        else:
          place += 1
          counter += 1
      if counter == len_of_word:
        return(the_word, len_of_word)

#checks wether player 2 guessed a letter right
def letter_check(guess, guessed_letters):
  while True:
    # Checking whether they put only one letter
    if len(guess) != 1:
      print("You can only do one letter at a time.")
      guess = input("Player 2, what letter do you guess? ")
    else:
      # Checking if they guessed a lower case letter
      if ord(guess) < 97 or ord(guess) > 122:
        print("You can only guess lowercase letters.")
        guess = input("Player 2, what letter do you guess? ")
      else: 
        # Checking if they already used that letter.
        counter = 0
        for i in range(18):
          if guess == guessed_letters[counter]:
            print("You've already used:", guess)
            guess = input("Player 2, what letter do you guess")
          else:
            counter += 1
        if counter == 18:
          return(guess)

#show how many lives are left
def life_system(lives):
  if lives == 6:
    print(HANGMAN_PICS[0])
  if lives == 5:
    print(HANGMAN_PICS[1])
  if lives == 4:
    print(HANGMAN_PICS[2])
  if lives == 3:
    print(HANGMAN_PICS[3])
  if lives == 2:
    print(HANGMAN_PICS[4])
  if lives == 1:
    print(HANGMAN_PICS[5])


  

"""
Don't worry about the code below, and don't change it.

It's just a way to trigger the `play_hangman` function
when you run this file from the command line.
"""
if __name__ == "__main__":
    play_hangman()
