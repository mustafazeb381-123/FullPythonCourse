"""
iterable - __iter__() or __getitem__()
iterator - __next__()
iteration -
"""
def gen(n):
    for i in range(n):
        yield (i)
g = gen(5)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# for i in g:
#     print(i)

m = "Mustafa"
abc = iter(m)
# print(abc.__next__())
# print(abc.__next__())
# print(abc.__next__())
# print(abc.__next__())
# print(abc.__next__())
# print(abc.__next__())
# print(abc.__next__())
for a in m:
    print(a)