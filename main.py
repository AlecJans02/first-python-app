mathOperation = input("What Math Operation Would You Like to Perform? Addition, Subtraction, Multiplication, Division or Modulo?: ")

def addition():
    input_a = (input("please enter first number: "))
    value_a = float(input_a)
    input_b = (input("please enter second number: "))
    value_b = float(input_b)
    total_value = (value_a + value_b)
    if isinstance(total_value, float):
        print("The two numbers given added together total" + " " + str(total_value))
    else: 
        print("one or both of the values are not numbers")

def subtraction():
    input_a = (input("please enter first number: "))
    value_a = float(input_a)
    input_b = (input("please enter second number: "))
    value_b = float(input_b)
    total_value = (value_a - value_b)
    if isinstance(total_value, float):
        print("The two numbers given subtracted total" + " " + str(total_value))
    else: 
        print("one or both of the values are not numbers")

def multiply():
    input_a = (input("please enter first number: "))
    value_a = float(input_a)
    input_b = (input("please enter second number: "))
    value_b = float(input_b)
    total_value = (value_a * value_b)
    if isinstance(total_value, float):
        print("The two numbers given multiplied will equal" + " " + str(total_value))
    else: 
        print("one or both of the values are not numbers")

def devide():
    input_a = (input("please enter first number: "))
    value_a = float(input_a)
    input_b = (input("please enter second number: "))
    value_b = float(input_b)
    total_value = (value_a / value_b)
    if isinstance(total_value, float):
        print("The two first value devided by the second value will equal" + " " + str(total_value))
    else: 
        print("one or both of the values are not numbers")

def modulo():
    input_a = (input("please enter first number: "))
    value_a = float(input_a)
    input_b = (input("please enter second number: "))
    value_b = float(input_b)
    total_value = (value_a % value_b)
    if isinstance(total_value, float):
        print("The remainder of the first value when diving the seconf value will equal" + " " + str(total_value))
    else: 
        print("one or both of the values are not numbers")



if(mathOperation == "Addition") :
    addition()
elif(mathOperation == "Subtraction"):
    subtraction()
elif(mathOperation == "Multiplication"):
    multiply()
elif(mathOperation == "Division"):
    devide()
elif(mathOperation == "Modulo"):
    modulo()
else:
    print("Please select one of the math operations listed above")


