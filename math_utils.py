def add_numbers(a: int, b: int) -> int:
    """Adds two numbers"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    return a + b
```

However, the above solution will still not work because the math_utils module is not installed. To fix this, you need to install the math_utils module or modify the tests to run without it. 

If you want to run the tests with the math_utils module, you can install it by running `pip install .` in the project directory if you're using a setup.py file, or by running `pip install -e .` if you're using a setup.cfg file.

If you want to modify the tests to run without the math_utils module, you can define the add_numbers function directly in the test file. Here's how you can do it: