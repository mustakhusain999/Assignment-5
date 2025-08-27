# Task 1: Create a Dictionary of Student Marks

# Step 1: a dictionary create where names are keys and marks are values

students = {'Alice':85, 'Boby':90, 'Charlie':65}

# Step 2: Ask for user input
name = input("Enter a student's name: ")

# Step 3 & 4: show marks or show "not found"
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")