
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number: "))
calculation = input("Please select the calculation from add and sub: ")

if calculation == "add":
    def add():
        addition = num1 + num2
        print(addition)
    add()
else:
    def sub():
        subtraction = num1-num2 
        print(subtraction)
    sub()

print("program executed completely")


