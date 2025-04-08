# in mathematics nx(n+1)/2

def sumn(x):
    if (x==0):
     return 0
    return x + sumn(x-1)
n =int(input(f"enter the value :"))
print(f"the febonacci value of {n} is {sumn(n)}")
