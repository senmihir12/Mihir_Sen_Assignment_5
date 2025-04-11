Task 1 - Create a dictionary of student marks
Creating a dictionary by taking random student names and marks - dict = {'Alice':85,'Ram':78,'Shyam':89,'Rohan':91,'Mohan':65}
Declaring a variable 'a' to enter string inputs of student's name - a = str(input("Enter the student's name: "))
If-else statement to see if student name 'a' in dictionary as one of the keys
if a in dict:
    print(a+"'s marks:",dict[a])
else:
    print("Student not found.")
Also adding 'Student not found' if student name not found


Task 2 - Demonstrate List Slicing
Entering numbers as a list from 1 to 10 - numbers = list(range(1,11))
Original list - print("Original list:",numbers)
Only first five elements - print("Extracted first five elements:",numbers[0:5])
Reversing these five elements - print("Reversed extracted elements:",numbers[4::-1])
