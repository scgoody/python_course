# Starter code for encoding a sequence of numbers
# Sarah Goodyear
# 3/4/2025
 

# Step 1: Prompt the user to input a sequence of numbers, separated by spaces

user_input = input("Enter a sequence of numbers separated by spaces: ")

 

# Step 2: Convert the input string into a list of integers
numbers = [int(num) for num in user_input.split()]
 

# Step 3: Define the transformation rules:

# - If the number is even, divide it by 2

# - If the number is odd, multiply it by 3 and add 1

def transform_number(n):
    if n % 2 == 0:
        return n // 2 # divides by 2 if even
    else:
        return n* 3 + 1 # mult. by 3 and add 1 if odd
 

# Step 4: Apply the transformation rules to each number in the sequence
transformed_sequence = [transform_number(num) for num in numbers]
 

# Step 5: Print the transformed sequence
print("Transformed sequence: ", transformed_sequence)
