"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = '730511294'

frequency = 0

wordle: str = input("Enter a 5-character word: ")

if len(wordle) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")

if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for "+ letter + " in " + wordle)

if letter == wordle[0]:
    print(letter + " found at index 0")
    frequency = frequency + 1   

if letter == wordle[1]:
    print(letter + " found at index 1")
    frequency = frequency + 1
    
if letter == wordle[2]:
    print(letter + " found at index 2")
    frequency = frequency + 1

if letter == wordle[3]:
    print(letter + " found at index 3")
    frequency = frequency + 1

if letter == wordle[4]:
    print(letter + " found at index 4")
    frequency = frequency + 1

if frequency == 0:
    print("No instances of " + letter + " found in " + wordle)

if frequency == 1:
    print("1 instance of " + letter + " found in " + wordle)

if frequency == 2:
    print("2 instances of " + letter + " found in " + wordle)

if frequency == 3:
    print("3 instances of " + letter + " found in " + wordle)

if frequency == 4:
    print("4 instances of " + letter + " found in " + wordle)

if frequency == 5:
    print("5 instances of " + letter + " found in " + wordle)