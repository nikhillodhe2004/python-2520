a=10
b=20
print(a+b)

x= None 
print(type(x))

#if else statments 
age = 20
if age >= 18:
    print("You can Vote")
else:
    print("You cannot Vote")

# input() : used to take input from keyboard
name = input("Enter Your Name: ")
print("Welcome: "+name)

age = input("Enter Your Age: ")
age = int(age)
if age >= 18: # # TypeError: '>='x not supported between instances of 'str' and 'int'
    print("You can Vote")
else:
    print("You cannot Vote")
