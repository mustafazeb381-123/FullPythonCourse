m = open("Mustafa.txt")
# print(m.tell())
m.seek(21)
print(m.readline())
print(m.tell())

print(m.readline())
print(m.tell())
print(m.readline())
m.close()
#seek is use for the 