def recur(x):
    if x == 0 or x == 1:
        return 1
    return x * recur(x - 1)
n = int(input("Enter the value of x: "))
print(f"The factorial of {n} is {recur(n)}")
