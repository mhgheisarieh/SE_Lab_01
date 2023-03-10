a = 0
b = 0
status = 0
operation = 0

def process_input(input):
    global a, b, status, operation
    if status == 0:
        print("Enter the operator:")
        a = int(input)
        status = 1
        return
    if status == 1:
        if input == "+":
            operation = 1
        elif input == "-":
            operation = 2
        elif input == "*":
            operation = 3
        elif input == "/":
            operation = 4
        else:
            print("Invalid operator")
            print("Enter the operator:")
            return
        print("Enter second operand:")
        status = 2
        return
    if status == 2:
        b = int(input)
        if operation == 1:
            print("a + b is: " + str(a + b))
        if operation == 2:
            print("a - b is: " + str(a - b))
        if operation == 3:
            print("a * b is: " + str(a * b))
        if operation == 4:
            print("a / b is: " + str(a / b))
        operation = 0
        status = 0
        print("Enter first operand:")



print("Enter first operand:")
while(True):
    input_ = input()
    if input_ == 'end':
        break
    process_input(input_)
