"""
MadLibs
Author: Noah Crandall
Period/Core: 2
"""


"""
Setup
"""
import time
import random

print("")

# Table of Contents
# first_name = 0
# last_name = 1
# adjective = 2
# adverb = 3
# food = 4
# place = 5
# verb = 6
# noun = 7
# name_of_fake_foreign_place = 8
# number = 9

again = 0

dream_vacation_blanks = [0, 2, 2, 3, 4, 5, 6, 7, 8]
dream_vacation_answers = ["place holder" for i in range(len(dream_vacation_blanks))]

love_letter_blanks = [0, 0, 1, 1, 2, 2, 6, 7, 9, 5]
love_letter_answers = ["place holder" for i in range(len(love_letter_blanks))]

store_advertisement_blanks = [0, 2, 2, 2, 2, 2, 5, 7, 8, 9, 9]
store_advertisement_answers = ["place holder" for i in range(len(store_advertisement_blanks))]

secret_prompt_blanks = [[0, 0, 0], 
[1, 1, 1], 
[2, 2, 2], 
[3, 3, 3], 
[4, 4, 4], 
[5, 5, 5], 
[6, 6, 6], 
[7, 7, 7], 
[8, 8, 8], 
[9, 9, 9]] #secret prompt for the user to find
secret_prompt_answers = [["place holder" for i in range(len(secret_prompt_blanks [a]))] for a in range(len(secret_prompt_blanks))] 

def ask_to_fill(prompt_chosen_blanks, prompt_chosen_answers): # Function asks user to fill in a detail in the story 
  while prompt_chosen_blanks != ["skip" for i in range(len(prompt_chosen_blanks))]:
    filler = random.randint(0,(len(prompt_chosen_blanks)-1))

    if prompt_chosen_blanks [filler] == 0:
      answer = input("Give me a first name: ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 1:
      answer = input("Give me a last name: ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 2:
      answer = input("Give me an adjective: ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 3:
      answer = input("Give me an adverb ending in 'ly': ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 4:
      answer = input("Give me a food: ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 5:
      answer = input("Give me a public place you could walk to: ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 6:
      answer = input("Give me a verb that doesn't end in ing: ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 7:
      answer = input("Give me a noun: ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 8:
      answer = input("Give me the name of a fake foriegn place: ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

    elif prompt_chosen_blanks [filler] == 9:
      answer = input("Give me a number: ")
      del prompt_chosen_answers [filler]
      (prompt_chosen_answers).insert (filler, answer)
      del prompt_chosen_blanks [filler]
      (prompt_chosen_blanks).insert (filler, "skip")

def ask_to_fill_secret_prompt():
  while secret_prompt_blanks != [["skip" for i in range(len(secret_prompt_blanks [0]))],
  ["skip" for i in range(len(secret_prompt_blanks [1]))],
  ["skip" for i in range(len(secret_prompt_blanks [2]))],
  ["skip" for i in range(len(secret_prompt_blanks [3]))],
  ["skip" for i in range(len(secret_prompt_blanks [4]))],
  ["skip" for i in range(len(secret_prompt_blanks [5]))],
  ["skip" for i in range(len(secret_prompt_blanks [6]))],
  ["skip" for i in range(len(secret_prompt_blanks [7]))],
  ["skip" for i in range(len(secret_prompt_blanks [8]))],
  ["skip" for i in range(len(secret_prompt_blanks [9]))]]:

    filler_one = random.randint(0,(len(secret_prompt_blanks)-1))

    filler_two = random.randint(0,(len(secret_prompt_blanks [filler_one])-1))

    if secret_prompt_blanks [filler_one [filler_two]] == 0:
      answer = input("Give me a first name: ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")

    elif secret_prompt_blanks [filler_one [filler_two]] == 1:
      answer = input("Give me a last name: ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")

    elif secret_prompt_blanks [filler_one [filler_two]] == 2:
      answer = input("Give me an adjective: ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")

    elif secret_prompt_blanks [filler_one [filler_two]] == 3:
      answer = input("Give me an adverb ending in 'ly': ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")

    elif secret_prompt_blanks [filler_one [filler_two]] == 4:
      answer = input("Give me a food: ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")

    elif secret_prompt_blanks [filler_one [filler_two]] == 5:
      answer = input("Give me a public place you could walk to: ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")

    elif secret_prompt_blanks [filler_one [filler_two]] == 6:
      answer = input("Give me a verb that doesn't end in ing: ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")

    elif secret_prompt_blanks [filler_one [filler_two]] == 7:
      answer = input("Give me a noun: ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")

    elif secret_prompt_blanks [filler_one [filler_two]] == 8:
      answer = input("Give me the name of a fake foriegn place: ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")

    elif secret_prompt_blanks [filler_one [filler_two]] == 9:
      answer = input("Give me a number: ")
      del secret_prompt_answers [filler]
      (secret_prompt_answers).insert (filler, answer)
      del secret_prompt_blanks [filler]
      (secret_prompt_blanks).insert (filler, "skip")


def reset(): # Resets everything
  dream_vacation_blanks = [0, 2, 2, 3, 4, 5, 6, 7, 8]
  dream_vacation_answers = ["place holder" for i in range(len(dream_vacation_blanks))]

  love_letter_blanks = [0, 0, 1, 1, 2, 2, 6, 7, 9, 5]
  love_letter_answers = ["place holder" for i in range(len(love_letter_blanks))]

  store_advertisement_blanks = [0, 2, 2, 2, 2, 2, 5, 7, 8, 9, 9]
  store_advertisement_answers = ["place holder" for i in range(len(store_advertisement_blanks))]

"""
Setup
"""

print("Let's play Silly Sentences!")
print("")
time.sleep(0.75)

while again != "n" and again != "no":
  print("You can choose to complete one of three prompts. Would you like to do Dream Vacation, Love Letter, or Store Advertisement?")
  prompt = (input(str())).lower()
  time.sleep(0.1)

  if prompt == "dream vacation" or prompt == "dreamvacation" or prompt == "dream_vacation":
    print("")
    ask_to_fill(dream_vacation_blanks, dream_vacation_answers)
    time.sleep(0.5)

    print("")
    print(dream_vacation_answers [0], "had always wanted to go to", dream_vacation_answers [8], "for as long as they could remember. The first thing they would do is ", dream_vacation_answers [6], "in the nearest", dream_vacation_answers [5], "all day long.\n\n", dream_vacation_answers [0] + ", when they would finish", dream_vacation_answers [8] + "ing in the", dream_vacation_answers[5], ", would try some of", dream_vacation_answers [8] + "'s world famous", dream_vacation_answers [1], dream_vacation_answers [4] + ". A common legend surrounding the", dream_vacation_answers [1], dream_vacation_answers [4], "is that if you can eat it as", dream_vacation_answers [3], "as you can, you will stumble upon a", dream_vacation_answers [2], dream_vacation_answers [7] + ".\n\nThe one catch is that you must remain in", dream_vacation_answers [8] + " for the rest of you days if you decide to take the", dream_vacation_answers [2], dream_vacation_answers [7] + ". The possibility of this didn't bother", dream_vacation_answers [0] + ". In fact, it would be a good thing since they so deeply wanted to go, staying the rest of their life would be a bonus!")
    print("")

    time.sleep(20)
    again = input("Would you like to play Silly Sentences again?").lower()
    reset()

  elif prompt == "love letter" or prompt == "loveletter" or prompt == "love_letter":
    print("")
    ask_to_fill(love_letter_blanks, love_letter_answers)
    time.sleep(0.5)

    print("")
    print("Dear Mr. & Mrs.", love_letter_answers [2] + ", \n\n\tI've written you this letter in order to tell you I wish to marry your beloved", love_letter_answers [1] + ". As you know, we have known eachother for some time and gone on approximately", love_letter_answers [8], "dates and are quite", love_letter_answers [4], "together. I have yet to tell", love_letter_answers [1], "as I want to keep it a surprise. I plan to do it on our next date when we are", love_letter_answers [6] + "ing by the", love_letter_answers [9] + ". I'll get down on one knee and propose with a", love_letter_answers [5], love_letter_answers [7] + ". It has been passed down and used to propose with through out my family. I would like to do this as soon as possible but want to receive your approval before doing so.\n\t\t\t\t\t\t\t\t\t\t\t\tFor your consideration,\n\t\t\t\t\t\t\t\t\t\t\t\t\t " + love_letter_answers [0], love_letter_answers [3])
    print("")

    time.sleep(20)
    again = input("Would you like to play Silly Sentences again?").lower()
    reset()

  elif prompt == "store advertisement" or prompt == "storeadvertisement" or prompt == "store_advertisement":
    print("")
    ask_to_fill(store_advertisement_blanks, store_advertisement_answers)
    time.sleep(0.5)

    print("")
    print(f"Come on down to {store_advertisement_answers [1]} {store_advertisement_answers [0]}'s {store_advertisement_answers [7]} Emporium. We've got every kind of {store_advertisement_answers [7]} in the great land of {store_advertisement_answers [8]}. {store_advertisement_answers [2]}, {store_advertisement_answers [3]}, {store_advertisement_answers [4]}, {store_advertisement_answers [5]}, we have them all in {store_advertisement_answers [1]} {store_advertisement_answers [0]}'s {store_advertisement_answers [7]} Emporium. Not only do we have the product, but we've got the deals. All my products are {store_advertisement_answers [9]} to {store_advertisement_answers [10]} cents cheaper than the competitors, and that's a {store_advertisement_answers [1]} {store_advertisement_answers [0]} promise. So come on down to {store_advertisement_answers [1]} {store_advertisement_answers [0]}'s {store_advertisement_answers [7]} Emporium, located next to your local {store_advertisement_answers [5]}")
    print("")

    time.sleep(20)
    again = input("Would you like to play Silly Sentences again?").lower()
    reset()

  elif prompt == "^^vv<><>abselectstart" or prompt == "^ ^ v v < > < > a b select start":
    time.sleep(1)

    print("Intruiging you thought that would do anything. I'm surprised you even thought to try it. I suppose you deserve something for finding this hidden dialouge but I should warn you, it will take a good chunk of time to do and may not even be worth it")
    time.sleep(1.5)
    secret_prompt_variable = input("Are you sure you want to complete the prompt? ").lower()

    if secret_prompt_variable == yes or secret_prompt_variable == y:
      ask_to_fill_secret_prompt()
      print("")
      time.sleep(2)

      print(f"")

  else:
    print("You'll need to answer with one of the three choices")
  
print("Thanks for playing!")