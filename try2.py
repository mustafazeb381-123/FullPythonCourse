f1 = open("Mustafa.txt")

try:
    f = open("Mustafa2.txt")
except Exception as e:
    print(e)
else:
    print("If the except is not print then the else is printing")
finally:
    print("this will print in anyway")
    # f.close()
    f1.close()
print("important stuff")