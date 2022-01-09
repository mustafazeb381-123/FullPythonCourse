# i = 0
# while(True):
#     if i+1<5:
#         i = i+1
#         continue
#     print(i+1, end=",")
#     if(i==44):
#         break
#     i = i + 1
while(True):
    inp = int(input("eneter the no\n"))
    if inp>100:
        print("congrates u  have entered greater than 100")
        break
    else:
        print("try again!")
        continue