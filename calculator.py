num_1 = float(input("Enter first number:"))
num_2 = float(input("Enter second number:"))
operation = input("Enter mathematical operation (+, -, *, /):")
if operation == "+":
    print(num_1 + num_2)
elif operation == "-":
    print(num_1 - num_2)
elif operation == "*":
    print(num_1 * num_2)
elif operation == "/":
    print(num_1 / num_2) 
    if num_2 == 0:
        print("Error: Cnnot divide by zero")
    else:
        print(num_1 / num_2)
else: 
    print("Error: Invalid operation")
    
git add .
git commit -m "Added my document"
git push origin main
