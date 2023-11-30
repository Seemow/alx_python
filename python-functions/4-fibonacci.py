def fibonacci_sequence(n):
    if n <= 0:
        return []  
    elif n == 1:
        return [0]  
    elif n == 2:
        return [0, 1] 

    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth number
    for i in range(2, n):
        fib_sequence.append(fib_sequence[n-i])

    return fib_sequence

# Example usage:
n = 6
result = fibonacci_sequence(n)
print(result)