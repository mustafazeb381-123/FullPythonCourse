# m = open("Mustafa2.txt","w")
# # m = open("Mustafa2.txt","a")
# a = m.write("Mustafa is athlete\n")
# print(a)
# m.close()

# handle read and write both.
m = open("Mustafa2.txt", "r+")
print(m.read())
m.write("thank you")