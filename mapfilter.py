#..........MAP..........
# numbers = ["43","65","55"]
# numbers = list(map(int,numbers))
# numbers[2] = numbers[2] + 1
# print(numbers[2])
# def sq(a):
#     return a*a
# num = [2,3,4,5,6,76,3,9]
# square = list(map(sq,num))
# print(square)
# num = [2, 3, 4, 5, 6, 76, 8, 9]
# square = list(map(lambda x:x*x,num))
# print(square)
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)
# ..........FILTER..........
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# def is_greater_5(num):
#     return num>=5
# gr_than_5 = list(filter(is_greater_5,list_1))
# print(gr_than_5)
#............REDUCE.............
from functools import reduce
list1 = [1, 2, 3, 4]
num = reduce(lambda x,y:x+y, list1)
print(num)
"""
num = 0
for i in list1:
    num = num + i
print(num)
"""