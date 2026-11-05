# Student Marks Analyzer

print("Student Marks Analyzer")

# Take marks for 5 subjects
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
marks4 = float(input("Enter marks for Subject 4: "))
marks5 = float(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total = marks1 + marks2 + marks3 + marks4 + marks5

# Intentional bug for testing phase: dividing by 4 instead of 5
percentage = total / 5

# Display the result
print("\n--- Result ---")
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
