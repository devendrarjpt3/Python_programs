w=5
w%=3
print(w)
print("________________")
v=50
v//=11
print(v)
print("________________")
print(x:=9)
z = isinstance(x, int)
print(z)
x**=2
print (f"square of 9 is {x}")
print("________________")
y=5  #101 in binary
y &= 3 #and operator in binary(101 & 011 = 001)
print(y)
a=5
a|=3
print(a)  # or operator  in binary (101 || 011 = 111)
b=5
b^=3
print(b) # XOR of (101 and 011= 110)
c=5
c>>=3
print(c) # 3 left shift of binary (101 --->000)
d=5
d<<=3
print (d) # 3 left shift of binary (101 ---> 101000)
#comparision operators
l=5
m=6
print(l==m)
print(l>m)
print(l<m)
print(l!=m)
#python logical operators
print(l<m and m>l)
print(not(l<m and m>l))
print(l>m or m<l)
#python identity operators
x=["apple", "banana"]
print("apple" in x)
print("orange" not in x)
#python bitwise operators
print(6&3)
print(6|3)
print(6^3)
print(100+~3)




