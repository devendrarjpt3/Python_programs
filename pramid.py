def fec(x):

    for i in range (1, x+1):
        for k in range (1, x-i+1):
         print(" ", end="")
        for j in range (1, i+1):
         print ("*", end=" ")
        print ()
    for i in range (x, 0, -1):
        for k in range (1, x-i+1):
         print(" ", end="")
        for j in range (1, i+1):
         print ("*", end=" ")
        print ()    
y = int(input("Entre the value:"))
fec(y)
