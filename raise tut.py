# a = input("what is your name")
# b = input("How much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stop the program")
# if a.isnumeric():
#     raise Exception("Number are not allowed")
# print(f"hello {a}")

c = input("Enter the name")
try:
    print(a)
except Exception as e:
    if c == "shahid":
        raise ValueError("shahid is blocked by mahnoor")
    print("Exception Handling")