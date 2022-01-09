# Lamda function or annonymous function
# def add(a,b):
#     return a+b
# minus = lambda x,y:x-y
# def minus(x,y):
#     return x-y
# print(minus(8, 5))

# def a_first(a):
#     return a[1]

a = [[1,4],[67,8],[2,5]]
a.sort(key=lambda x:x[1])
# a.sort(key=a_first)
print(a)