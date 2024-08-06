from fibonacci import fibonacci, fibonacci_recursive, is_fibonacci

def main():
    print("First 10 Fibonacci numbers:")
    print(fibonacci(10))

    print("\nFirst 10 Fibonacci numbers (recursive):")
    print(fibonacci_recursive(10))

    test_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("\nTesting if numbers are in the Fibonacci sequence:")
    for num in test_numbers:
        print(f"{num}: {is_fibonacci(num)}")

if __name__ == "__main__":
    main()
