file = open("test.txt","r")
i = file.read()
file.close()
try:
    print(i)
    i = int(i)
    i = i +1
    file = open("test.txt","w")
    file.write(str(i))
    file.close()
except:
    i = 1
    file = open("test.txt","w")
    file.write(str(i))
    file.close()
