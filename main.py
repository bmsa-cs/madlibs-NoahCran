"""
MadLibs
Author: 
Period/Core:


"""

# Requirements
"""
Prompts match up with the order the words are used in the story.

At least 8 inputs

Inputs should use a variety of parts of speech (noun, adjective, verb, etc.) and/or specific types of nouns (place, food, etc.)

Has proper spelling and grammar

Is at least 4+ sentences long.

Using the input() function, prompt the user to, "Enter a name: ", then assign and store their response to a variable.

Repeat benchmark 2 for the other 8 inputs that we need from the user: adjective, adjective, adverb, food, food, noun, place, and verb.

Using a print() function, output, "[name] was planning a dream vacation to [place]." Replace [name] and [place] with the proper variables.

Repeat step 4 with the other 6 lines of output.

Double-check to make sure the output is formatted correctly - including spaces before and after variables and line spacing.

Run and test your program with the values from the Sample Run.

Debug and repeat step 7 as needed.
"""
# Requirements

"""
Setup
"""
import time
import random

# Table of Contents
# first_name = 0
# last_name = 1
# adjective = 2
# adverb = 3
# food = 4
# place = 5
# verb = 6
# noun = 7
# proper_noun = 8

again = str("yes")

dream_vacation_blanks = [0, 2, 2, 3, 4, 4, 5, 6, 7]
dream_vacation_answers = ["place holder" for i in range(len(dream_vacation_blanks))]

love_letter_blanks = [] #fill in later
love_letter_answers = ["place holder" for i in range(len(love_letter_blanks))]

store_advertisment_blanks = [] #fill in later
store_advertisment_answers = ["place holder" for i in range(len(love_letter_blanks))]

def ask_to_fill(prompt_chosen_blanks, prompt_chosen_answers): # Function asks user to name part of speech 
  while prompt_chosen_blanks != ["skip" for i in range(len(prompt_chosen_blanks))]:
    filler = random.randint(0,(len(prompt_chosen_blanks)-1))

    if prompt_chosen_blanks [filler] == 0:
      answer = input("Give me a first name:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 1:
      answer = input("Give me a last name:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 2:
      answer = input("Give me an adjective:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 3:
      answer = input("Give me an adverb:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 4:
      answer = input("Give me a food:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 5:
      answer = input("Give me a place:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 6:
      answer = input("Give me a verb:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 7:
      answer = input("Give me a noun:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 8:
      answer = input("Give me a name to a store:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 9:
      answer = input("Give me a number:")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

def reset(): # Resets everything
  dream_vacation_blanks = [0, 2, 2, 3, 4, 4, 5, 6, 7]
  dream_vacation_answers = ["place holder" for i in range(len(dream_vacation_blanks))]

  love_letter_blanks = [] #fill in later
  love_letter_answers = ["place holder" for i in range(len(love_letter_blanks))]

  store_advertisment_blanks = [] #fill in later
  store_advertisment_answers = ["place holder" for i in range(len(love_letter_blanks))]

"""
Setup
"""

print("Let's play Silly Sentences!")
print("")
time.sleep(0.75)

while again != "n":
  print("You can choose to complete one of three prompts. Would you like to do Dream Vacation, Love Letter, or Store Advertisment?")
  prompt = (input(str())).lower()

  if prompt == "dream vacation" or prompt == "dreamvacation" or prompt == "dream_vacation":
    print("")
    ask_to_fill(dream_vacation_blanks, dream_vacation_answers)
    
    again = input("Would you like to play Silly Sentences again?").lower()

  elif prompt == "love letter" or prompt == "loveletter" or prompt == "love_letter":
    print("LL") #delete later

    again = input("Would you like to play Silly Sentences again?").lower()

  elif prompt == "store advertisment" or prompt == "storeadvertisment" or prompt == "store_advertisment":
    print("SA") #delete later

    again = input("Would you like to play Silly Sentences again?").lower()

  else:
    print("N/A") #delete later

  reset()
  
print("Thanks for playing!")