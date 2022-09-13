def love(subject: str) -> str:
    return f" I love you {subject}!"
"""Given a subject as a parameter, returns a loving string"""


def spread_love(to: str, n: int) -> str:
    love_note: str = ""
    counter: int = 0
    while counter < n:
        love_note = love_note + love(to) + "\n"
        counter = counter + 1
    return love_note

    """Generates a str repeating a loving message n times"""
print("Hello\nworld\n!!!")
