
import random
from hangman_word import word_list 
from hangman_art import logo,stages


lives = 6
chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}.")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess =  input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
            end_of_game = True
            print("You win!")
    
    from hangman_art import stages
    print(stages[lives])