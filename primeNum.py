n = int(input("Enter a number, which you check prime or not:"))

if n == 1:
    print("You entered 1, which is neither prime nor composite")
else:
    is_prime = True  # Assume the number is prime initially
    for i in range(2, n):
        if n % i == 0:
            is_prime = False  # If a divisor is found, it's not prime
            break  # No need to check further, we found a divisor
    
    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
