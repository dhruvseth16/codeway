'''Design a simple calculator with basic arithmatic operations. 
Prompt the user to input to numbers and an operation of choice. 
Perform the calculations and display the result.'''


while True:       
    num1 = float(input("Enter the first number: "))        
    opt = input("Enter the arithmatic operation you want to do (/, * ,+, -):  ")
    num2 = float(input("Enter the second number: "))

    if opt == "/":
        result = num1/num2
        break
    elif opt == "+":
        result = num1+num2
        break
    elif opt == "-":
        result = num1-num2
        break
    elif opt == "*":
        result = num1*num2
        break
    else: 
        print ("Please select from /, *, -, +")
    

print (result)



