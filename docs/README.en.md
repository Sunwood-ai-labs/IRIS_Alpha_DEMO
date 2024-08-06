# IRIS_Alpha_DEMO

[![Release](https://raw.githubusercontent.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/main/.github/release_notes/header_image/release_header_latest.png)](https://raw.githubusercontent.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/main/.github/release_notes/header_image/release_header_latest.png)

# Latest Release Notes:

## IRIS Release Notes - Version v1.1.0

Release Date: 2024-08-06

## New Features

- Added Fibonacci sequence generation functionality.
    - `fibonacci(n)` function to return a Fibonacci sequence of a specified number.
    - `fibonacci_recursive(n)` function using a recursive approach.
    - `is_fibonacci(num)` function to determine if a given number is included in the Fibonacci sequence.
- Added examples of Fibonacci sequence generator usage.
    - Examples demonstrating the use of `fibonacci(n)`, `fibonacci_recursive(n)`, and `is_fibonacci(num)` functions can be found in `examples/fibonacci_examples.py`.

## Changes

- Fixed the header font family when generating release notes.
    - Previously, "Times New Roman" was used, but there was a problem that it was not displayed correctly in some environments.
    - By using "DejaVu Math TeX Gyre" from now on, display compatibility in many environments has been improved.
- Removed unnecessary log output.
    - Removed unnecessary log output settings from `translate_readme.py` and `generate_header_image.py`.

---

# Repository Summary:
# Project: IRIS_Alpha_DEMO

```
OS: posix
Directory: /home/runner/work/IRIS_Alpha_DEMO/IRIS_Alpha_DEMO

├─ examples/
│  ├─ fibonacci_examples.py
├─ fibonacci.py
├─ issue_creator.log
├─ README.md
```

## .

`fibonacci.py`

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = fibonacci_recursive(n - 1)
    fib.append(fib[-1] + fib[-2])
    return fib

def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num
```

`issue_creator.log`

```
```

`README.md`

```markdown
# IRIS_Alpha_DEMO
```

## .github

`.github/labels.csv`

```
label,description
bug,Something isn't working
documentation,Improvements or additions to documentation
duplicate,This issue or pull request already exists
enhancement,New feature or request
feature,New feature or request
good first issue,Good for newcomers
help wanted,Extra attention is needed
invalid,This doesn't seem right
question,Further information is requested
wontfix,This will not be worked on
```

---

<!-- Automated update --># Last updated: Tue Aug  6 11:29:15 UTC 2024 - Release: v1.1.0 - Run ID: 10265646027
<!-- Automated update -->