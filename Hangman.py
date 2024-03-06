import random

categories = ["planet", "fruit", "shape"]


def choose_word(category):

    if category == categories[0]:
        words = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
    elif category == categories[1]:
        words = ["apple", "banana", "orange", "strawberry", "grape", "pineapple", "watermelon"]
    elif category == categories[2]:
        words = ["circle", "square", "triangle", "rectangle", "pentagon", "hexagon", "octagon"]
    else:
        print("Invalid.")
        return hangman()
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    print("Select a category: (" + ", ".join(categories) + ")")
    category = input("You: ").lower()

    word = choose_word(category)
    if word is None:
        return

    guessed_letters = []
    attempts = 6

    print("Guess the word with a letter only (" + "_" * len(word) + ")")

    while attempts > 0:
        guess = input("You: ").lower()

        if len(guess) != 1:
            attempts -= 1
            print(f"Only 1 letter at a time. You have {attempts} attempts left.")
            if attempts == 0:
                print("Game over! The word was:", word)
                return
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            if attempts == 0:
                print("Game over! The word was:", word)
                return

        print("Guess the word with a letter only (" + display_word(word, guessed_letters) + ")")

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            return


print("Welcome to Hangman!")
hangman()
