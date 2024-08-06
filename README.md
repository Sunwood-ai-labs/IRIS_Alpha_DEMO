# Project: IRIS_Alpha_DEMO

## IRIS Release Notes - Version v2.1.0

Release Date: 2024-08-07

## New Features

- Implemented a Fibonacci sequence game. (#98ff204)
    - This interactive game allows users to learn about the Fibonacci sequence in a fun way.
    - Users can take a Fibonacci quiz, check if a number is in the Fibonacci sequence, and find the nearest Fibonacci number.
- Added tests for the Fibonacci sequence game. (#986a892)
    - This ensures that the game is working as expected.

## Changes

- Improved the accuracy of README automatic updates. (#ba47ee3)
    - Added update guidelines to the LLM prompt during README auto-update.
    - This is expected to generate a README that reflects more accurate and up-to-date information.
- Updated English README. (#10cbb4a, #a720325)
- Updated header images.

## Fixes

- Fixed the header font family when generating release notes. (#f60687d)
    - Previously, "Times New Roman" was used, but there was a problem that it was not displayed correctly in some environments.
    - From now on, by using "DejaVu Math TeX Gyre", display compatibility in many environments has been improved.
- Removed unnecessary log output. (#f60687d)
    - Removed unnecessary log output settings from `translate_readme.py` and `generate_header_image.py`.

---

# Fibonacci Fun

This repository is an interactive Python project that allows you to have fun learning about the Fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. 

This project provides various functions and a game to explore the Fibonacci sequence.

## Features

- **Generate Fibonacci numbers:** Get a list of the first N Fibonacci numbers.
- **Check Fibonacci membership:** Determine if a given number is a Fibonacci number.
- **Find nearest Fibonacci:** Find the closest Fibonacci number to a given number.
- **Interactive Fibonacci Game:** Test your knowledge and learn about the Fibonacci sequence through an engaging game!

## Getting Started

### Prerequisites

- Python 3.6 or higher

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

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.# Last updated: Tue Aug  6 11:42:25 UTC 2024 - Release: v2.1.0 - Run ID: 10265829843
<!-- Automated update -->
