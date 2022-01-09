# l = 10#Global
# def function1(n):
#     # l = 5#local
#     global l
#     l = l + 45
#     m = 8#local
#     print(l, m)
#     print(n, "i have printed")
# function1("this is me")
# # print(l)
x = 10
def mustafa():
    x= 20
    def shahid():
        global x
        x= x+23
    print("brfore calling shahid()",x)
    shahid()
    print("after calling shahid()",x)
mustafa()
print(x)