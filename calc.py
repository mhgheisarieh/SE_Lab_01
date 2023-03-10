a = 0
b = 0
status = 0
operation = 0

def process_input(input):
    global a, b, status, operation
    if status == 0:
        a = int(input)
        status = 1
        return
    if status == 1:
        if input == "+":
            operation = 1
        if input == "-":
            operation = 2
        if input == "*":
            operation = 3
        if input == "/":
            operation = 4
        status = 2
        return
    if status == 2:
        b = int(input)
        if operation == 1:
            print(a + b)
        if operation == 2:
            print(a - b)
        if operation == 3:
            print(a * b)
        if operation == 4:
            print(a / b)
        operation = 0


while(True):
    input_ = input()
    if input_ == 'end':
        break
    process_input(input_)
