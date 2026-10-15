# Student Marks Calculator

print("===== Student Marks Calculator =====")

# Enter The Student Name

student_name = input("Enter Student Name: ")

# Student Marks Calculator

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Validate Marks
if (sub1 < 0 or sub1 > 100 or
    sub2 < 0 or sub2 > 100 or
    sub3 < 0 or sub3 > 100):

    print("Invalid Marks! Enter marks between 0 and 100.")

else:
    # Calculate Total and Average Marks
    total_marks = sub1 + sub2 + sub3
    average_marks = total_marks / 3

    # Calculate Grade checking

    if 75 <= average_marks <= 100:
        grade = "A"
    elif 65 <= average_marks < 75:
        grade = "B"
    elif 55 <= average_marks < 65:
        grade = "C"
    elif 35 <= average_marks < 55:
        grade = "S"
    elif 0 <= average_marks < 35:
        grade = "F"
    else:
        grade = "Invalid Marks"

    # Display Results

    print("\n===== Results =====")
    print(f"Student Name: {student_name}")
    print(f"Subject 1 Marks: {sub1}")
    print(f"Subject 2 Marks: {sub2}")
    print(f"Subject 3 Marks: {sub3}")
    print(f"Total Marks: {total_marks:.2f} / 300")
    print(f"Average marks: {average_marks:.2f}%")
    print(f"Grade: {grade}")
