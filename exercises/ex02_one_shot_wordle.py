"""Ex02 - One Shot Wordle!"""
__author__ = '730511294'
SECRET: str = "python"
length: int = len(SECRET)
guess: str = input(f"What is your {length}-letter guess? ")

i: int = 0
outcome: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
while len(guess) != len(SECRET):
    guess = input(f"That was not {length} letters! Try again: ")

while i < len(SECRET):
    if guess[i] == SECRET[i]:
        outcome = outcome + GREEN_BOX
    else:
        present: bool = False
        location: int = 0
        while not present and location < len(SECRET):
            """Established a new int variable so that we can go through the index's of the word without affecting the previous variable"""
            """Run's every i character that didn't print a green box through every location within the word to see if it is elsewhere.   """
            if guess[i] == SECRET[location]:
                present = True
                """When the varaible is swtiched to True, once the loop finishes every place it prints a yellow box"""
            else:
                location = location + 1
        if present:
            outcome = outcome + YELLOW_BOX
        else:
            outcome = outcome + WHITE_BOX
    i = i + 1
    """This allows the entire code to run again off the original while loop, as it goes through every index of the word."""
print(outcome) 
if guess != SECRET:
    print("Not quite. Play again soon!")
if guess == SECRET:
    print("Woo! You got it!")
