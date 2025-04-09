dict = {'Alice':85,'Ram':78,'Shyam':89,'Rohan':91,'Mohan':65}
a = str(input("Enter the student's name: "))
if a in dict:
    print(a+"'s marks:",dict[a])
else:
    print("Student not found.")