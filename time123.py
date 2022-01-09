# Time module
import time
initial = time.time()
k=0
while(k<45):
    print("This is Mustafa")
    # time.sleep(1)
    k+=1
print("while loop is ran",time.time() - initial,"second")
initial2 = time.time()
for i in range(45):
    print("this is shahid")
print("for loop is ran", time.time() - initial2,"second")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
