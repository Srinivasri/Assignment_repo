num1 = float (input("Enter the first number:"))
num2 = float (input("Enter the second number:"))
operator = (input ("Enter operator:(+,-,*,/):"))
if operator == "+":
 result = num1 + num2
elif operator == "-":
 result = num1 - num2
elif operator == "*":
 result = num1 * num2
elif operator == "/":
    if num2 == 0:
       print ("number 0 is not divisable")
    else:
       result = num1 / num2 

else :
 print ("unknown operator")
 result = None

if result is not None:
 print ( "result=", result)


if result is not None:
 print ( "result=", result)

 if result > 0:
        print ("Positive")
 elif result < 0:
        print ("Negative")
 else:
        print ("Zero")
