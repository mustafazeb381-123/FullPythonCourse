# no of guesses 9
#print no gueeses left
#no of guesses he took to finish
#game over
print("Enter the no")
n = 9
while(True):
    n2 = int(input())
    if n2>9:
        print("decrease the no")
    elif n2<9:
        print("increse the no")
    elif n2==9:
        print("congrates u have done")
        break
    else:
        print("try again")
        continue