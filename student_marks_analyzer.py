def calculate_percentage(total):
    # Calculates percentage out of 500 total marks (5 subjects)
    return (total / 500) * 100

if __name__ == "__main__":
    print("Student Marks Analyzer")
    marks1 = float(input("Enter marks for Subject 1: "))
    marks2 = float(input("Enter marks for Subject 2: "))
    marks3 = float(input("Enter marks for Subject 3: "))
    marks4 = float(input("Enter marks for Subject 4: "))
    marks5 = float(input("Enter marks for Subject 5: "))

    total = marks1 + marks2 + marks3 + marks4 + marks5
    percentage = calculate_percentage(total)

    print("\n--- Result ---")
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
