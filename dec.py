# def function1():
#     print("it's me")
# func2 = function1
# del function1
# func2()

# def functret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# # a = functret(0)
# a = functret(1)
# print(a)

# def exrcutor(func):
#     func("this")
# exrcutor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec
@dec1
def who_is_me():
    print("who is me")
# who_is_me = dec1(who_is_me)
who_is_me()