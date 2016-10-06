equation=input("Enter and equation:")
operation=equation[1]
number1=float(equation[0])
number2=float(equation[2])

if operation =="*":
    print("The result is " + str(number1*number2));
elif operation =="+":
    print("The result is " + str(number1+number2));
elif operation=="-":
    print("The result is " + str(number1-number2))
elif operation=="/":
    print("The result is " + str(number1/number2));
elif operation=="%":
    print("The result is " + str(number1%number2))