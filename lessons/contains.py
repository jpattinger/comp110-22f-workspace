"""Example implementing a list utility function"""

# Function name: contains
# We will have 2 parameters: needle (str), haystack (list[str])
# Return type bool
# Gameplan:
# 1
def contains(needle:str, haystack: list[str]) -> bool:
    #Gameplan
    #1. Start with the first index
    i: int = 0
    #2. Loop trhough every index
    while i < len(haystack):
    #   2.a: Test if iterm at index equal to needle
        if haystack[i] == needle:
    #   2.a: True Return True! We found it!
            return True
        i += 1
    # 3. Return False
    return False
