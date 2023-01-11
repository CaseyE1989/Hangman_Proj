import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
display = []
end_of_game = False
lives = 6
previous_guess = []

print(hangman_art.logo)

for _ in range(len(chosen_word)): #Display blanks '_','_','_'
    display += '_'
print(display)

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    for position in range(len(chosen_word)): # Displays letters if guess is correct
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    print(display)

    if guess in previous_guess:
        print(f'You chose {guess}. You chose that already. Please, try another letter.')
    elif guess in display:
        print(f'You chose {guess}.')
        previous_guess.append(guess)
    elif guess not in display:
        lives -= 1
        print(f'You chose {guess}. The letter is not in the answer. You lose a life!')
        previous_guess.append(guess)
        print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True
        print('You win!')
    elif lives == 0:
        end_of_game = True
        print('You lose!')
        print(f'The word was {chosen_word}.')
        input()
