def fibonacci_sequence(n):
    if n <= 0:
        return []  
    
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence
