# for loop
# list1 = [["mustafa","16"],["shahid","13"],["hammad","12"],["zeeshan","17.5"],["wassi","15"]]
# dict1 = dict(list1)
# for item in dict1:
#     print(item)
# print(dict1)
#for item, size in list1:
# for item, size in dict1.items():
#     print(item, "bicep is  ", size)
#Quiz by harry
list2 = [int, float, "mustafa", 1, 3, 34, 43, 56, 544, 6, 9]
for item in list2:
    if str(item).isnumeric() and item>=6:
        print(item)