n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))