# Student Grade Analyzer

def calculate_average(marks):
    return sum(marks) / len(marks)


def find_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"


def analyze_marks(marks):
    avg = calculate_average(marks)
    grade = find_grade(avg)
    highest = max(marks)
    lowest = min(marks)

    print("\n--- Result ---")
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)


# Main Program
marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

analyze_marks(marks)


# Example Output:
# Enter number of subjects: 5
# Enter marks for subject 1: 85
# Enter marks for subject 2: 90
# Enter marks for subject 3: 78
# Enter marks for subject 4: 88
# Enter marks for subject 5: 76
#
# --- Result ---
# Marks: [85, 90, 78, 88, 76]
# Average: 83.4
# Grade: B
# Highest Marks: 90
# Lowest Marks: 76
