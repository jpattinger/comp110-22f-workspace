"""The Complete Wordle!"""
__author__ = '730511294'


def contains_char(word: str, letter: str) -> bool:
    """Finds the character anywhere in the word while going through every index"""
    """Makes sure that the letter str is always equal to 1"""
    """Returns true if the letter is found, which we use in the following function"""
    assert len(letter) == 1
    index: int = 0
    while index < len(word):
        if word[index] == letter:
            return True
        index += 1
    return False
   

def emojified(guess: str, secret: str) -> str:
    """Makes sure that the lens of guess is equal to secret word"""
    """If index of guess and secret are equal the result includes a green box"""
    """Otherwise, runs through the contains_char function to see if its in the word or not"""
    assert len(guess) == len(secret)
    White_Box: str = "\U00002B1C"
    Yellow_Box: str = "\U0001F7E8"
    Green_Box: str = "\U0001F7E9"
    result: str = ""
    index: int = 0
    while index < len(secret):
        if guess[index] == secret[index]:
            result += Green_Box
        else:
            if contains_char(secret, guess[index]):
                result += Yellow_Box
            else:
                result += White_Box
        index += 1
    return result


def input_guess(expected_length: int) -> str:
    """Asks the user to set an expected length of the guess, check to make sure it is right length"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    """Uses all of the previous fucntions in a main loop"""
    """Prints the turn number with an increment after every guess"""
    """input guess verifies the length"""
    """emojified function holds onto the return statments and then prints it"""
    turn_number: int = 1
    guess: str = ""
    secret: str = "codes"
    while turn_number <= 6 and guess != secret:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn_number}/6 turns!")
        elif turn_number == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turn_number += 1

if __name__ == "__main__":
    main()

