import random

choice = ["rock", "paper", "scissors"]

matches = {
    "rock": {"rock": "draw", "paper": "lose", "scissors": "win"},
    "paper": {"rock": "win", "paper": "draw", "scissors": "lose"},
    "scissors": {"rock": "lose", "paper": "win", "scissors": "draw"},
}


def choose():
    global choice
    n = random.randint(0, 2)
    return choice[n]


def playerchoose():
    global choice
    playerchoice = input("Rock, paper, or scissors?\n")
    while playerchoice not in choice:
        print(f"{playerchoice} not valid!\n")
        playerchoice = input("Rock, paper, or scissors?\n")
    return playerchoice


def decide(playerwins, compwins):

    a = playerchoose()
    b = choose()
    print(f"\nYou chose {a}, computer chose {b}")
    outcome = matches[a][b]
    if outcome == "win":
        print("You win this round!")
        playerwins += 1
    elif outcome == "lose":
        print("You lose this round!")
        compwins += 1
    else:
        print("It's a draw!")
    print(f"Your score: {playerwins}, computer score: {compwins}\n")
    return playerwins, compwins


def main():
    playerwins = 0
    compwins = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Best two out of three.\n")

    while playerwins < 2 and compwins < 2:
        playerwins, compwins = decide(playerwins, compwins)
    if playerwins == 2:
        print("You win the game!!")
    elif compwins == 2:
        print("You lose the game. :(")

    print("Thanks for playing! :)")


if __name__ == "__main__":
    main()
