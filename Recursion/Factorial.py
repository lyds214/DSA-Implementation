def factorialRecursion(n):
    if n <= 0:
        return 
    if n == 1:
        return n
    
    return n * factorialRecursion(n - 1)

def factorialIterative(n):
    fact = 1 

    for num in range(2, n - 1):
        fact += num 
    
    return fact

print(factorialRecursion(5))