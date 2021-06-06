import time
import os
from hangman_art import *
from hangman_words import *


def main():
    logo = HangmanArt().get_logo()
    invalid_trail = 5
    chosen_word = WordList().get_chosen_word()
    alphabets = WordList().get_alphabets()
    lives = len(HangmanArt()) - 1
    game_is_finished = False
    word_length = len(chosen_word)

    clear()
    print(logo)
    time.sleep(1)
    display = ["-" for x in range(word_length)]

    while not game_is_finished:
        guess = input("Guess a letter: ").lower()
        clear()

        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = chosen_word[position]
        print("="*15*word_length + "\n")
        print("HANGMAN"+ "\n")
        print("="*15*word_length + "\n")
        print("THE WORD!!" + "\n")
        print("+"*15*word_length + "\n")
        print(f"{' '.join(display)}\n")
        print("+"*15*word_length + "\n")
        print("DISPLAY\n")
        print("-" * 15 * word_length + "\n")

        if len(guess) == 1 and guess.isalpha():
            if guess not in chosen_word and guess in alphabets:
                if lives != 1:
                    print(f"You guessed '{guess}', that's not in the word. You lose a point.\n")
                lives -= 1
                if lives == 1:
                    hint = input("Do you need a hint? 1.Yes 2.No\n").lower()
                    if hint == '1' or hint == 'yes':
                        alphabets[alphabets.index(guess)] = "*"
                        not_chosen_word = 5
                        while not_chosen_word != 0:
                            char_to_remove = random.choice(alphabets)
                            if (char_to_remove not in chosen_word) and char_to_remove != "*":
                                alphabets[alphabets.index(char_to_remove)] = '*'
                                not_chosen_word -= 1
                        clue = [x for x in alphabets if x != '*']
                        print("Here are the clues for the remaining characters\n")
                        print(clue)
                    else:
                        pass
                if lives == 0:
                    game_is_finished = True
                    print("I am sorry, You lost the game!!.\n")
                    print(f"The word is {chosen_word}")
            elif guess not in alphabets:
                print(f"You've already guessed {guess}. Please guess another character\n")
            if guess in alphabets:
                alphabets[alphabets.index(guess)] = '*'
                #print("GEN")
                #print(alphabets)
        else:
            invalid_trail, game_is_finished = trail_timeout(guess, invalid_trail, chosen_word)

        if '-' not in display:
            game_is_finished = True
            print("You win.\n")
        print("-"*15*word_length + "\n")
        #print(chosen_word)
        print("="*15*word_length + "\n")
        print("HANGMAN\n")
        print("="*15*word_length + "\n")
        print(HangmanArt().get_stages(lives)+ "\n")


def trail_timeout(guess, invalid_trail, chosen_word):
    if len(guess) == 1 or not guess.isalpha() or len(guess) != 1 and guess.isalpha():
        invalid_trail -= 1
        print("Please Enter a valid input\n")
    if invalid_trail == 0:
        print("you have exceeded the allowed wrong input limit\n")
        print("I am sorry, You lost the game!!.\n")
        print(f"The word is {chosen_word}")
        return invalid_trail, True
    else:
        return invalid_trail, False


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
