def fibonacciRecursion(n):
    if n < 0:
        return  
    
    if n == 0:
        return 0 

    if n == 1 or n == 2:
        return 1 
    
    else:
        return fibonacciRecursion(n - 1) + fibonacciRecursion(n - 2)

def fibonacciIterative(n):
    a = 0
    b = 1 

    for x in range(1, n):
        c = a + b 
        a = b 
        b = c 
    
    return b


print(fibonacciIterative(9))
print(fibonacciRecursion(9))

