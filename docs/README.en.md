# Project: IRIS_Alpha_DEMO

## IRIS Release Notes - Version v2.1.0

Release Date: 2024-08-07

## New Features

- **Fibonacci Sequence Game:** An interactive game designed to teach users about the Fibonacci sequence in a fun way. (#98ff204)
    - Features a Fibonacci quiz.
    - Allows users to check if a number belongs to the Fibonacci sequence.
    - Enables finding the nearest Fibonacci number to a given input. 
- **Tests for Fibonacci Sequence Game:** Ensures the game functions as intended. (#986a892)

## Changes

- **Improved README Auto-Update Accuracy:** Enhanced the precision of automatic README updates. (#ba47ee3)
    - Introduced update guidelines for the LLM prompt during the auto-update process.
    - This aims to generate a more accurate and current README.
- **Updated English README:** Made revisions to the English README file. (#10cbb4a, #a720325)
- **Updated Header Images:** Refreshed the header images.

## Fixes

- **Header Font Family in Release Notes:** Fixed an issue with the header font family when generating release notes. (#f60687d)
    - "Times New Roman" was previously used but encountered display problems in certain environments.
    - Switched to "DejaVu Math TeX Gyre" to improve display compatibility across various environments.
- **Removed Unnecessary Log Output:** Eliminated redundant log output settings. (#f60687d)
    - Removed these settings from `translate_readme.py` and `generate_header_image.py`.

---

# Fibonacci Fun

This repository hosts an interactive Python project that makes learning about the Fibonacci sequence enjoyable.

The Fibonacci sequence is a series of numbers where each number is calculated by adding the two numbers before it. The sequence begins with 0 and 1.

This project provides a variety of functions and a game to help you explore the Fibonacci sequence.

## Features

- **Generate Fibonacci numbers:** Generate a list containing the first N Fibonacci numbers.
- **Check Fibonacci membership:** Determine whether a given number is a Fibonacci number.
- **Find nearest Fibonacci:** Identify the Fibonacci number closest to a provided number.
- **Interactive Fibonacci Game:** Put your knowledge to the test and learn more about the Fibonacci sequence through an engaging game!

## Getting Started

### Prerequisites

- Python 3.6 or a later version

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fibonacci-fun.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fibonacci-fun
   ```

### Usage

1. **Import the functions:**

   ```python
   from fibonacci import fibonacci, is_fibonacci, find_nearest_fibonacci
   ```

2. **Use the functions:**

   ```python
   # Generate the first 10 Fibonacci numbers
   fib_numbers = fibonacci(10) 
   print(fib_numbers)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

   # Check if a number is a Fibonacci number
   is_fib = is_fibonacci(13) 
   print(is_fib)  # Output: True

   # Find the nearest Fibonacci number
   nearest_fib = find_nearest_fibonacci(12)
   print(nearest_fib)  # Output: 13
   ```

3. **Play the Fibonacci Game:**

   ```bash
   python fibonacci_game.py
   ```

   Follow the on-screen instructions to play the game.

## Contributing

We welcome contributions! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. For more details, please refer to the LICENSE file.

# Last updated: Tue Aug  6 11:42:25 UTC 2024 - Release: v2.1.0 - Run ID: 10265829843
<!-- Automated update -->