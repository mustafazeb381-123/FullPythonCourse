# F string
import math
me = "Mustafa"
a1 = 3
# a = "this %s %s "%(me, a1)
# a = "this is {1}{0}"
# b = a.format(me, a1)
# print(b)
a =f" this is {me} {a1} {math.cos(65)}"
print(a)