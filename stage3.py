student_name = (input("Enter the Student Name:"))
subject1 = int (input("Enter the Subject 1 Marks:"))
subject2 = int (input("Enter the Subject 2 Marks:"))
subject3 = int (input("Enter the Subject 3 Marks:"))
percentage =float(((subject1 +subject2+subject3)/300) * 100)

print (student_name)
print ("Total :",subject1 + subject2 + subject3,"/300")
print ("Percentage :", percentage , "%" )
if percentage >= 75:
 print ("Grade : A")
elif percentage >= 60:
 print ("Grade : B")
elif percentage >= 40:
 print ("Grade : C")
else:
 print ("Grade : F")