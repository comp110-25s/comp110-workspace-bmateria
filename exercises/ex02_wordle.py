"""Create the game wordle using what we have learned in COMP110!"""

__author__: str = "730476994"

# emoji box codes used throughout the program
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret_word: str, character: str) -> bool:
    """determine whether character is in secret word"""
    # code can only run if character has a length of 1
    assert len(character) == 1, f"len('{character}') is not 1"
    # the while loop will continue until every character in secret_word is checked
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] != character:
            idx = idx + 1
        else:
            return True
    return False


def emojified(guess: str, secret_word: str) -> str:
    """return color based on character's presence and position"""
    assert len(guess) == len(secret_word), "Guess must be same length as secret"
    # emojis will be added to the end of emoji_string with each iteration of while loop
    emoji_string: str = ""
    idx: int = 0
    while idx < len(secret_word):
        if guess[idx] == secret_word[idx]:
            emoji_string = emoji_string + GREEN_BOX
            idx = idx + 1
        elif contains_char(secret_word=secret_word, character=guess[idx]):
            emoji_string = emoji_string + YELLOW_BOX
            idx = idx + 1
        else:
            emoji_string = emoji_string + WHITE_BOX
            idx = idx + 1
    return emoji_string


def input_guess(N: int) -> str:
    """ensure input string is proper length"""
    # the user is prompted to input a word
    input_word: str = input(f"Enter a {N} character word:")
    # while loop will run until the word the user inputs matches the desired length
    while len(input_word) != N:
        input_word = input(f"That wasn't {N} characters! Try again:")
    return input_word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # local variables will keep track of the user's progress in the game
    turns: int = 1
    won: bool = False
    while turns < 7 and not won:
        print(f"=== Turn {turns}/6 ===")
        input_word = input_guess(len(secret))
        print(emojified(guess=input_word, secret_word=secret))
        if input_word == secret:
            print(f"You won in {turns}/6 turns!")
            won = True
            turns = 7
        elif turns == 6:
            print("X/6 - Sorry, try again tomorrow!")
            won = False
            turns = 7
        else:
            turns = turns + 1
            won = False


if __name__ == "__main__":
    main(secret="codes")
