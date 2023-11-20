def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return"Cannot divide by zero"
    return a/b

print("Simple Calculator")
print("Operations:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=input("Enter operation (1/2/3/4):")
n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))

if choice=='1':
    print("Result:",add(n1,n2))
elif choice=='2':
    print("Result:",subtract(n1,n2))
elif choice=='3':
    print("Result:",multiply(n1,n2))
elif choice=='4':
    print("Result:",divide(n1,n2))
else:
    print("Invalid input")
