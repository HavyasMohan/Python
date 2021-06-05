from hangman_art import *
from hangman_words import *
import os


def main():
    logo = HangmanArt().get_logo()
    chosen_word = WordList().get_chosen_word()
    print(chosen_word)
    alphabets = WordList().get_alphabets()
    lives = len(HangmanArt()) - 1
    game_is_finished = False
    word_length = len(chosen_word)

    display = ["-" for x in range(word_length)]

    while not game_is_finished:
        guess = input("Guess a letter: ").lower()
        clear()

        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = chosen_word[position]
        print(f"{' '.join(display)}")

        if guess not in chosen_word and guess in alphabets:
            print(f"You guessed '{guess}', that's not in the word. You lose a point.")
            lives -= 1
            if lives == 0:
                game_is_finished = True
                print("I am sorry, You lost the game!!.")
        elif guess not in alphabets:
            print(f"You've already guessed {guess}. Please guess another character ")

        if len(guess) == 1 and guess.isalpha():
            if guess in alphabets:
                alphabets[alphabets.index(guess)] = '*'

        if '-' not in display:
            game_is_finished = True
            print("You win.")

        print(HangmanArt().get_stages(lives))






def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
