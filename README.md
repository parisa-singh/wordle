# Word Guessing Game

## Overview

This Python program is a simple word-guessing game where the player attempts to guess a randomly selected word from a predefined list. The game provides feedback on each guess, indicating whether each letter in the guess matches the solution in the correct position.

## Features

1. **Interactive Gameplay**  
   - Players are prompted to guess a 5-letter word.
   - Feedback is given for each guess with visual indicators.
2. **Feedback System**  
   - **🟢**: Correct letter in the correct position.
   - **🔴**: Incorrect letter or wrong position.
3. **Random Word Selection**  
   - The solution word is randomly chosen from a predefined list of common words.
4. **Victory Condition**  
   - If the player guesses the word correctly, the game ends with a congratulatory message.
5. **Attempts Limit**  
   - Players have up to 6 attempts to guess the word. If unsuccessful, the solution is revealed.
     
## Requirements

- Python 3.x

## How to Play

1. **Run the Game**  
   Execute the script in a terminal or an IDE.

2. **Guess the Word**  
   - You will be prompted to guess a 5-letter word.
   - Input your guess and press **Enter**.

3. **Interpret the Feedback**  
   - Each letter in your guess will receive feedback:
     - **🟢**: Correct letter in the correct position.
     - **🔴**: Incorrect letter or wrong position.

4. **Win or Lose**  
   - If you guess the word correctly, you win!
   - If you fail after 6 attempts, the solution is revealed.

## Functions Explained

### **Core Functions**

1. **`get_guess()`**  
   Prompts the user to input a guess and converts it to uppercase for uniformity.

2. **`print_word(word)`**  
   Displays the guessed word with each letter separated by a space.

3. **`exact_match_compare(solution, guess)`**  
   Compares the player's guess with the solution and returns a string of indicators:
   - **🟢** for correct matches.
   - **🔴** for incorrect matches.

4. **`one_turn(solution)`**  
   Executes one turn of the game:
   - Prompts the user for a guess.
   - Displays the guess and feedback.
   - Checks if the guess matches the solution and ends the game if correct.

5. **`make_solution()`**  
   Randomly selects a word from a predefined list of 10 words.

## Example Gameplay

### Start of Game
```
What word is this?: FIRST
F I R S T
🔴🔴🔴🔴🟢
```

### After Multiple Guesses
```
What word is this?: OTHER
O T H E R
🟢🟢🟢🔴🔴
```

### Win Scenario
```
What word is this?: WHICH
W H I C H
🟢🟢🟢🟢🟢
Congratulations!
```

### Loss Scenario
```
Word was "AFTER", better luck next time.
```

## Customization

1. **Word List**  
   Modify the list in `make_solution()` to include more or different words:
   ```python
   words = ["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"]
   ```

2. **Word Length**  
   This program supports only 5-letter words. Update the word list and adjust the logic in functions if you want to support other lengths.

## Contributions

Feel free to fork this repository, suggest improvements, or report any issues.

## License

This project is open-source and available under the MIT License.
