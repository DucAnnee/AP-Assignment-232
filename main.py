### Lambda functions ###
square = lambda x: x ** 2
print(square(5))  # Output: 25


### Higher-Order functions ###
numbers = [1, 2, 3, 4, 5]

# Use map() to apply a function to each element
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Use filter() to create a new list with elements that satisfy a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Use reduce() to perform a rolling computation on a sequence
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15


### List Comprehensions ###
numbers = [1, 2, 3, 4, 5]

# Create a new list with squared values
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Filter for even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]


### Generators and Generator Expressions ###
# Generator function
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

counter = count_up_to(5)
print(list(counter))  # Output: [0, 1, 2, 3, 4]

# Generator expression
numbers = (x ** 2 for x in range(5))
print(list(numbers))  # Output: [0, 1, 4, 9, 16] 