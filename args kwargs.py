# def function_name_print(a, b, c, d):
#     print(a, b, c, d)
# function_name_print("Mustafa", "shahid", "hammad", "Romi")
def funargs(normal, *argsshahid, **kwargs):
    print(normal)
    print(type(argsshahid))
    for item in argsshahid:
        print(item)
    print("now would like i will introduce my freinds")
    for key, value in kwargs.items():
        print(key, value)
har = ["mustafa", "shahid", "hammad", "romi"]
kw =  {"hammad":"javacoder","shahid":"android devloper", "noman":"all rounder of coding",
       "mustafa":"beginner of pycoding"}
normal = "i am a normal Argument and student are:"
funargs(normal, *har, **kw)