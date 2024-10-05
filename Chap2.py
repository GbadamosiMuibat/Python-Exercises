#Write a program that prints your name 100 times.
for i in range(100):
 print("My name is Muhibah Gbadamosi")
 
 
 
#Write a program to fill the screen horizontally and vertically with your name. 
# [Hint: add the option end='' into the print function to fill the screen horizontally.]
for i in range(100):
    print("My name is Muhibah Gbadamosi", end='')
    
#Write a program that prints out a list of the integers from 1 to 20 and their squares. 
for i in range(1,21):
    print(i+1,"The square of the number is:",i*i)
    
#Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.
for i in range(5,87):
    print("The number increased by three is: ", i+3)
    

#Write a program that asks the user for their name and how many times to print it.
#The program should print out the user’s name the specified number of times

name = input("Enter your name: ")
name_time = int(input("How many times do you want your name to be printed: "))

for i in range(name_time):
    print(name)
    
#The Fibonacci numbers are the sequence below, where the first two numbers are 1, 
#and each number thereafter is the sum of the two preceding numbers. 
#Write a program that asks the user how many Fibonacci numbers to print and then prints that many.

X = int(input("How many fibonnacci number do you wnat to print: "))
fib1, fib2 = 1, 1
print(fib1, fib2, end=" ")

for i in range( 2, X):
    next_fib = fib1 + fib2
    print(next_fib, end=" ")
    
    fib1, fib2 = fib2 ,next_fib
