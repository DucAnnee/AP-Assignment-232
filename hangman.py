import random

def choose_word(word_list):
    return random.choice(word_list)


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)


def get_guessed_word(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])


def make_guess(guessed_letters, guess):
    return guessed_letters | {guess}


def get_remaining_attempts(word, guessed_letters, max_attempts):
    incorrect_guesses = len(
        [letter for letter in guessed_letters if letter not in word]
    )
    return max_attempts - incorrect_guesses


def hangman(word_list, max_attempts=6):
    word = choose_word(word_list)
    guessed_letters = set()
    attempts_left = max_attempts

    def game_loop(guessed_letters, attempts_left):
        print("\nWord to guess:", display_word(word, guessed_letters))
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            return game_loop(guessed_letters, attempts_left)

        guessed_letters = make_guess(guessed_letters, guess)
        attempts_left = get_remaining_attempts(word, guessed_letters, max_attempts)

        if is_word_guessed(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            return
        elif attempts_left <= 0:
            print("Sorry, you ran out of attempts. The word was:", word)
            return
        else:
            return game_loop(guessed_letters, attempts_left)

    game_loop(guessed_letters, attempts_left)

word_list = ["functional", "programming", "python", "hangman"]

hangman(word_list)