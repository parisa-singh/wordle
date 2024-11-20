# Author: Parisa Singh
# Email: parisasingh@umass.edu
# Spire ID: 34751702

import random
# part a
def get_guess(): 
    guess = input ("What word is this?: ")
    return guess.upper()
# part b
def print_word(word):
    print(' '.join(word))
# part c
def exact_match_compare(solution, guess):
    result = ''
    for sol_letter, guess_letter in zip(solution, guess):
        if sol_letter == guess_letter:
            result += '🟢'
        else:
            result += '🔴'
    return result
# part d
def one_turn(solution):
    guess = get_guess()
    print_word(guess)
    match_result = exact_match_compare(solution, guess)
    print(match_result)
    if guess == solution:
        print("Congratulations!")
        exit()
# part e 
def make_solution():
    words = ["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"]
    return random.choice(words)
# play the game
soln = make_solution()
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
print(f"Word was \"{soln}\", better luck next time.")