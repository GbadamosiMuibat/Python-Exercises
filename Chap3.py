# Write a program that generates and 
# prints 50 random integers, 
# each between 3 and 6.

import random
random_integers = [random.randint(3,6) for i in range(50)]
print(random_integers)

# Write a program that generates a random number, x, between 1 and 50, a random number y
#between 2 and 5, and computes x^y.

x = random.randint(1,50)
y = random.randint(2,5)
result = x ** y
print(x,y,result)

# Write a program that generates a random number 
# between 1 and 10 and prints your name that many times.

random_numbers = random.randint(1,10)

name = input("Enter your name: ")

for i in range(random_numbers):
    print(name)
    
# Write a program that asks the user for a number 
# and prints out the factorial of that number
def factorial(n):
    if n == 1 or n == 1:
     return 1
    else:
      return n * factorial(n-1)  
  
user = eval(input('Enter a number: '))
result = factorial(user)
print(f"The factorial of {user} is {result}.")



num = int(input("Enter a number: "))
#The factorial is assign i because the factorial of one and zero is 1
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print(f"The factorial of {num} is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")

# Write a program that asks the user for a number and 
# then prints out the sine, cosine, and tangent of that number

import math

angle_degrees = float(input("Enter an angle in degrees: "))

angle_radians = math.radians(angle_degrees)

sine_value = math.sin(angle_radians)
cosine_value = math.cos(angle_radians)
tangent_value = math.tan(angle_radians)

print(f"Sine of {angle_degrees} degrees: {sine_value:.4f}")
print(f"Cosine of {angle_degrees} degrees: {cosine_value:.4f}")
print(f"Tangent of {angle_degrees} degrees: {tangent_value:.4f}")
