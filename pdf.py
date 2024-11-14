# Using the + operator
greeting1 = "Hello"
greeting2 = "World"
full_greeting = greeting1 + ", " + greeting2 + "!"
print(full_greeting)  # Output: Hello, World!

# Using an f-string
name = "World"
formatted_greeting = f"Hello, {name}!"
print(formatted_greeting)  # Output: Hello, World!


string = "this is a string in python"

# First character
print(string[0])  # Output: t

# Last character
print(string[-1])  # Output: n


# Corrected function definition
def reverse_string(input_string):
    return input_string[::-1]  # This slices the string to reverse it

# Asking for user input and calling the function
user_input = input("Enter string: ")
reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)


def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_contants = 0
    
    for char in text:
        pass
    return (num_vowels, num_contants)

input_text = input("Enter a string: ")
result = count_vowels_and_consonants(input_text)
print("Vowels and consonants:", result)


def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Test the function
even_or_odd(3)  # Output: Odd
even_or_odd(4)  # Output: Even


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())


def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test the function
fizz_buzz(15)
