# Nguyễn Bá Chung, mssv 245752021610143
# 9. Chương trình máy tính thực hiện các phép tính đơn giản
# This function adds two numbers
def add(x, y):
 return x + y
# This function subtracts two numbers
def subtract(x, y):
 return x - y
# This function multiplies two numbers
def multiply(x, y):
 return x * y
# This function divides two numbers
def divide(x, y):
 return x / y
print("Select operation.")
print("1.cộng")
print("2.trừ")
print("3.nhân")
print("4.chia")
# Take input from the user
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
 print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
 print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
 print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
 print(num1,"/",num2,"=", divide(num1,num2))
else:
 print("Invalid input")
