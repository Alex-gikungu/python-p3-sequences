#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fibonacci_sequence = []
    elif length == 1:
        fibonacci_sequence = [0]
    else:
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < length:
            next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_num)
    print(fibonacci_sequence)

# Test the function
print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(9)
