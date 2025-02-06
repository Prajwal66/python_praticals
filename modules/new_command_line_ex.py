import sys

def add(a,b):
    return a + b


num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1,num2)
    print(output)

