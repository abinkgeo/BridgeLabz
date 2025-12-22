import math

A = int(input("Enter A value"))
B = int(input("Enter B Value"))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for num in range(A, B + 1):
    if is_prime(num):
        count += 1

print(count)
