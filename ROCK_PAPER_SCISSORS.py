import random

player = input("Enter any of the three letters, R, P or S: ")
my_list = ["R", "P", "S"]
CPU = random.choice(my_list)
if player == "R":
    print(f"Player: (ROCK)")
elif player == "S":
    print(f"Player: (SCISSORS)")
else:
    print(f"Player: (PAPER)")
if CPU == "R":
    print(f"Player: (ROCK)")
elif CPU == "S":
    print(f"Player: (SCISSORS)")
else:
    print(f"Player: (PAPER)")
print(f"CPU: {CPU}")

if player == "R":
    if CPU == "R":
        print("The game is draw")
    elif CPU == "S":
        print("Player  wins")
    else:
        print("CPU wins")
elif player == "S":
    if CPU == "R":
        print("CPU wins")
    elif CPU == "S":
        print("The game is draw")
    else:
        print("Player  wins")
else:
    if CPU == "R":
        print("Player  wins")
    elif CPU == "S":
        print("CPU wins")
    else:
        print("The game is draw")