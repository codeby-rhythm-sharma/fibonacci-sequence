#!/usr/bin/env python3
"""
fibonacci.py
Generates Fibonacci sequence up to n terms (iterative + memoized recursive).
Handles invalid input and edge cases.
"""

def fibonacci_iterative(n):
    """Return a list of the first n Fibonacci numbers using iteration."""
    if n <= 0:
        return []
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def fibonacci_recursive(n, memo=None):
    """Return F(n) using recursion with memoization (efficient)."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 0
        return 0
    if n == 1:
        memo[1] = 1
        return 1
    memo[n] = fibonacci_recursive(n-1, memo) + fibonacci_recursive(n-2, memo)
    return memo[n]

def generate_fibonacci_recursive(n):
    """Return a list of the first n Fibonacci numbers using memoized recursion."""
    if n <= 0:
        return []
    memo = {}
    return [fibonacci_recursive(i, memo) for i in range(n)]

def main():
    try:
        n = int(input("Enter number of terms (positive integer): ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    # Iterative (recommended for large n)
    iter_seq = fibonacci_iterative(n)
    print("\nIterative Fibonacci (first {} terms):".format(n))
    print(iter_seq)

    # Recursive (memoized) — fine for moderate n, shows alternative approach
    rec_seq = generate_fibonacci_recursive(n)
    print("\nRecursive (memoized) Fibonacci (first {} terms):".format(n))
    print(rec_seq)

    # Example: show nth Fibonacci number (0-based index)
    print("\nThe {}-th Fibonacci number (0-based index) is: {}".format(n-1, rec_seq[-1]))

if __name__ == "__main__":
    main()
