import random
from termcolor import colored

# Open .txt file containing five letter words and save words in a list
words_list = []
wordle_words = []
with open('wordlewords.txt') as f_obj:
    contents = f_obj.readlines()

for line in contents:
    words_list.append(line)

for word in words_list:
    wordle_words.append(word.strip())

# Computer picks a random 5 letter word
computer_word = wordle_words[random.randint(0,len(wordle_words))]

# Wordle Game

# Assigns colors to letters that are in the word
already_guessed = []
previous_guesses = []
def wordle(selection):
    output = ''
    for i in range(0,len(selection)):
        if selection[i] not in already_guessed:
            already_guessed.append(selection[i])
        if selection[i] == computer_word[i]:
            output += colored(selection[i],'grey', 'on_green', attrs=['bold'])
            continue
        elif selection[i] in computer_word:
            output += colored(selection[i], 'grey', 'on_yellow', attrs=['bold'])
            continue
        else:
            output += selection[i]
    print(output)
    already_guessed.sort()
    print(f'Letters guessed: {already_guessed}')

# Game loop
number_of_guesses = 0
while True:
    if number_of_guesses == 6:
        print(f"You lose... The word was '{computer_word}'. You used up all {number_of_guesses} guesses.")
        break
    guess = input("Please guess a 5 letter word: ")
    if len(guess) != 5:
        print('Please make sure your guess has 5 letters\n')
        continue
    elif guess.lower() not in wordle_words:
        print("Invalid word... \n")
        continue
    elif guess.lower() == computer_word:
        number_of_guesses += 1
        print(f"You win! The word was '{computer_word}'! You took {number_of_guesses} guesses.")
        break
    else:
        number_of_guesses += 1
        wordle(guess.lower())
