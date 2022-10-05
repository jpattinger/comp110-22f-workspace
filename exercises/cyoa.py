"""Choose your own adventure dungeon role playing simulator!"""
__author__ = '730511294'

health: int = 15
points: int = 10
player: str = ""
damage: int = 1
BULL_EMOJI: str = "\U0001F9AC"
OLD_WIZARD: str = "\U0001F9D9"
SWORD_EMOJI: str = "\U0001F5E1"
MEDAL_EMOJI: str = "\U0001F947"


def greet() -> None:
    """Welcomes the player to the game, on top of assigning the players name to the player name varaible."""
    print("Welcome adventurer, to the dungeon of the Minotaur!")
    print("If you can emerge victorious, the spoils will be yours.")
    global player
    player = input("Who believes that they are strong enough to vanquish this mighty foe? ")


def weapons() -> None:
    """One of two inital encounters, offers an exchance og plus damage for less points."""
    print(f"You encounter a traveler who is offering a weapon {SWORD_EMOJI} for sale.")
    print(f"Hello {player}, I've been expecting you. For 5 gold, you can have a broadsword that will upgrade your attack to 3. ")
    sword: str = input("Do you want the sword. Reply with yes or no: ")
    if sword == "yes":
        global points
        points -= 5
        global damage
        damage = 3
        print(f"You now have {points} gold coins.")
        print(f"Your damage has increased to {damage}.")


def old_man(player: str, points: int) -> int:
    """Second of two initial encounter, offers a bag that randomly does or doesn't cointain coins."""
    print(f"Walking down the hallway, you see an old shrouded man {OLD_WIZARD}. He offers you a bag, with no further commentary.")
    choice: str = input("Do you accept his offer? Reply with yes or no: ")
    if choice == "yes":
        import random
        bag: int = (random.randint(1, 2))
        if bag == 1:
            points += 5
            print(f"Your now have {points} gold coins.")
            print(f"Congratulations {player}.")
        else:
            print(f"Tough luck {player}, that was the empty bag.")
        return points
    else:
        print(f"I'm sorry to hear that {player}.")
        return points


def procedure() -> None:
    """Main interaction of the program that outlines the choice between two different rooms. Then depicts the battle with the minotaur and the dialogue leading up to it."""
    global points 
    global health
    global damage
    first_choice: str = ""
    first_choice = input("Would you like to take the left or right passage? If you wish to flee without any treasure, you may do that as well. Please reply with left, right, or flee: ")
    if first_choice == "flee":
        print("You escaped with 10 health and 0 gold.")
        return None
    if first_choice == "left":
        weapons()
    if first_choice == "right":
        health = old_man(player, points)
    print("Continuing down the passageway, it opens into a large dimly lit room.")
    print("Stirring from the floor where he was slumbering, the minotaur prepares to engage in battle!")
    print("Sitting behind him is a chest of gold coins patiently waiting to be removed from this dungeon, but to do so you will have to vanquish this foe.")
    print(f"Everytime you land a hit on the minotaur {BULL_EMOJI}  you will also receive coins.")
    m_health: int = 10
    m_damage: int = 2
    while m_health > 0 and health > 0:
        second_choice: str = input("Do you wish to attack, defend, or flee? ")
        if second_choice == "flee":
            print(f"You escaped with {health} health and {points} gold.")
            return None
        if second_choice == "attack":
            print("You struck a strong blow to the minotaur, but it gashed you as well!")
            m_health -= damage
            health -= m_damage
            points += damage
            print(f"The minotaur has {m_health} health, you have {health} health, and {points} gold coins.")
        if second_choice == "defend":
            import random
            print("The minotaur comes charging as you put up your sword in defense.")
            charge: int = (random.randint(1, 2))
            if charge == 1:
                print("You deflected his charge and struck a strong blow to his back.")
                m_health -= (2 * damage)
                points += (2 * damage)
                print(f"The minotaur has {m_health} health, you have {health} health, and {points} gold coins.")
            if charge == 2:
                print("The minotaur ignores your defensive attempts and tramples you.")
                health -= (2 * m_damage)
                print(f"You now have {health} health and {points} gold coins.")
    if m_health <= 0:
        print("Wow! You did it! You slayed the minotaur!")
        print("To the victor go the spoils")
        points += 100
        print(f"You emerged victorious with {points} gold {MEDAL_EMOJI}.")
        return None
    if health <= 0: 
        print("You were slain by the minotaur!")
        print("Who will be strong enough to defeat him!")
        return None
    

def main() -> None:
    """Main fucntion that simply transmits the code to the greeting and procedure fucntion."""
    greet()
    procedure()


if __name__ == "__main__":
    main()