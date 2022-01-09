#set in python
s = set()
#print(type(s))
# l = [1, 2, 3, 4]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))
s.add(1)
s.add(2)
#s1 = s.union({1,2,3})
#s1 = s.intersection({1, 2, 3})
s1 = {3,4}
print(s.isdisjoint(s1))
print(max(s))
print(min(s))
s.remove(1)
s.add(7)
print(s)