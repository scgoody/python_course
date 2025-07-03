# Starter code for calculating the average exam grade
#Student Name: Sarah Goodyear
#Date: 2/28/2025
#Assignment Title: calculating the average exam grade


# Step 1: Create a list of exam grades (replace [] with actual grades)
grades = [100,95,72,55,87,11,99,100,88,92,83,89]

# Step 2: Calculate the sum of the grades using the sum() function
sumGrades = sum(grades)

# Step 3: Find the number of grades using the len() function
numGrades = len(grades)

# Step 4: Compute the average (sum of grades / number of grades)
avgGrade = sumGrades / numGrades

# Step 5: Print the average to the console
print(f"Average exam grade: {avgGrade:.2f}")
