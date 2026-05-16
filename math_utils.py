def add_numbers(a: int, b: int) -> int:
    """Adds two numbers"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if isinstance(a, list) or isinstance(b, list):
        raise TypeError("Both inputs must be integers, not lists")
    return a + b
```

Note: The error in the pytest error output is due to the fact that pytest is not installed or not properly configured in the environment. However, since the math_utils module is not installed, we can't run the tests as is. We need to install the math_utils module or modify the tests to run without it. For the sake of this exercise, I'm assuming that the math_utils module is not installed and we need to modify the tests to run without it. 

However, if you want to run the tests with the math_utils module, you can install it by running `pip install .` in the project directory if you're using a setup.py file, or by running `pip install -e .` if you're using a setup.cfg file. 

Also, note that the add_numbers function in math_utils.py is not correctly handling non-integer inputs. It's raising a TypeError when the inputs are not integers, but it's not handling the case when the inputs are lists. We can modify the function to handle this case by adding a check for lists and raising a TypeError if the inputs are lists. 

Here's the modified function:
```python
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if isinstance(a, list) or isinstance(b, list):
        raise TypeError("Both inputs must be integers, not lists")
    return a + b
```

But since the inputs are already defined as integers in the test cases, this check is not necessary. The function will work correctly without it.