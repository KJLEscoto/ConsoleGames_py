import random


def generate_word_search(size, words):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for word in words:
        word = word.upper()
        direction = random.choice(directions)
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        while not is_valid_position(grid, x, y, direction, len(word)):
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        for letter in word:
            grid[x][y] = letter
            x += direction[0]
            y += direction[1]
    fill_empty_cells(grid)
    return grid


def is_valid_position(grid, x, y, direction, length):
    size = len(grid)
    x_end = x + (length - 1) * direction[0]
    y_end = y + (length - 1) * direction[1]
    if x_end < 0 or x_end >= size or y_end < 0 or y_end >= size:
        return False
    for i in range(length):
        if grid[x + i * direction[0]][y + i * direction[1]] != ' ':
            return False
    return True


def fill_empty_cells(grid):
    size = len(grid)
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice(letters)


def print_word_search(grid, underline):
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if (i, j) in underline:
                print('\033[4m' + letter + '\033[0m', end=' ')
            else:
                print(letter, end=' ')
        print()


def play_game(size, words):
    word_search_grid = generate_word_search(size, words)
    underline = set()
    found_words = set()
    remaining_words = set(words)
    while True:
        print("--- Word Search Puzzle ---")
        print_word_search(word_search_grid, underline)
        print()
        word = input("Enter the word you found (or 'exit' to quit): ").upper()
        if word == 'EXIT':
            break
        elif word in found_words:
            print()
            print("Already found that word. Try another!")
            continue
        found = find_word(word_search_grid, word)
        if found:
            print()
            print(f"Congratulations! '{word}' found!")
            underline |= found
            found_words.add(word)
            remaining_words.remove(word)
        else:
            print()
            print("Sorry, there is no word for that.")
        if not remaining_words:
            break
    print()
    print("---- Game Over! ----")
    print("List of found words:")
    print(", ".join(found_words) if found_words else "-")
    print("List of remaining words:")
    print(", ".join(remaining_words) if remaining_words else "-")


def find_word(grid, word):
    size = len(grid)
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, 1), (-1, -1)]
    for i in range(size):
        for j in range(size):
            for direction in directions:
                x, y = i, j
                found = set()
                for letter in word:
                    if x < 0 or x >= size or y < 0 or y >= size or grid[x][y] != letter:
                        break
                    found.add((x, y))
                    x += direction[0]
                    y += direction[1]
                if len(found) == len(word):
                    return found
    return None


size = 10
words = ['PYTHON', 'PROGRAM', 'WORD', 'SEARCH', 'PUZZLE', 'CONSOLE', 'GAME']
play_game(size, words)
