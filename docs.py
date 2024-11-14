def even_numbers(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

print(even_numbers([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]


def print_numbers():
    for num in range(10):
        if num == 5:
            continue
        if num == 8:
            break
        print(num)
        
print_numbers()


def find_five(nums):
    for num in nums:
        if num == 5:
            print("Found")
            break
    else:
        print("5 is not on the list")


find_five([1, 2, 3, 4])  # Output: "5 is not in the list."
find_five([1, 2, 5, 6])  # Output: "Found 5!"


def greet(name, greeting='Hello'):
    return f'{greeting}, {name}'

print(greet("Alice"))
print(greet("Bob", "Good day"))

def display_info(name, *, age=None):
    return f"Name: {name}, Age: {age}"

# Test the function
print(display_info("Alice", age=25))  # Output: "Name: Alice, Age: 25"


multiplyFn = lambda x, y: x * y

# Test the lambda function
print(multiplyFn(3, 4))  # Output: 12


def add(a, b):
    """Return the sum of two numbers."""
    return a + b

# Test the function and view the docstring
print(add(3, 5))       # Output: 8
print(add.__doc__)     # Output: "Return the sum of two numbers."


def multiply(a: int, b: int) -> int:
    return a * b

# Test the function
print(multiply(3, 5))  # Output: 15
