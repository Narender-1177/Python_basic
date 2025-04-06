def add(x ,y):
    print(x+y)

def substract(x ,y):
    print(x-y)

def multiply(x ,y):
    print(x*y)

def divide(x ,y):
    print(x/y)

def modulas(x ,y):
    print(x%y)  

def power(x ,y):
    print(x**y)    


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))     

print("calculator Menu: ")
print("Type 1 for Addition")
print("Type 2 for Substract")
print("Type 3 for Multiply")
print("Type 4 for Division")
print("Type 5 for Remainder")
print("Type 6 for Power")

num = int(input("Type here: "))

if num==1:
    add(number1, number2)
elif num==2:
    substract(number1, number2)
elif num==3:
    multiply(number1, number2) 
elif num==4:
    divide(number1, number2)
elif num==5:
    modulas(number1, number2)
elif num==6:
    power(number1, number2) 
else:
    print("Enter a Valid number.")                 