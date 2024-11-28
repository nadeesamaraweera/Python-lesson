#define find factorial without recursion

def find_factorial(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial *= i
        return factorial

print(find_factorial(10))


#define find factorial with recursion


def find_factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (x* find_factorial(x-1))

print(find_factorial(1000))