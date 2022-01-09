# Snake Water Gun

import random
print("Game started")
lst = ["Snake", "Water", "Gun"]
print("Enter 'S' for selecting 'Snake'")
print("Enter 'W' for selecting 'Water'")
print("Enter 'G' for selecting 'Gun'")
user_score = 0
comp_score = 0
chances = 10
while chances >= 1:
    comp_pick = random.choice(lst)
    user_pick = input().capitalize()
    if user_pick == "S":
        chances = chances - 1
        if comp_pick == "Snake":
            print("Draw!")
            continue
        elif comp_pick == "Water":
            print("You win!")
            user_score = user_score + 1
            continue
        else:
            print("Computer win!")
            comp_score = comp_score + 1
            continue
    elif user_pick == "W":
        chances = chances - 1
        if comp_pick == "Snake":
            print("Computer win!")
            comp_score = comp_score + 1
            continue
        elif comp_pick == "Water":
            print("Draw!")
            continue
        else:
            print("You win!")
            user_score = user_score + 1
            continue
    else:
        chances = chances - 1
        if comp_pick == "Snake":
            print("You win!")
            user_score = user_score + 1
            continue
        elif comp_pick == "Water":
            print("Computer win!")
            comp_score = comp_score + 1
            continue
        else:
            print("Draw!")
            continue

print("Game ended")
print("Your Score is",user_score)
print("Computer Score is", comp_score)

if user_score > comp_score:
    print("You won the game!")
elif comp_score > user_score:
    print("Computer won the game!")
else:
    print("It was draw!")