#Arithmetic 
result = ( 512 - 282 )/( 47 * 48 + 5 )
print("The Result is: ", result)


#Ask the user to enter a number. Print out the square of the number, 
# but use the sep optional argument to print it out in a full sentence that ends in a period.
##Ask the user to enter a number 
number =int(input(f"Enter a number: "))
square_root = number **2
print("The square root of the", number, " is: ", square_root)

#Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,and 5x, 
# each separated by three dashes

x = int(input("Enter a Number: "))
print(x, x*2, x*3, x*4, x*5,sep="---")


#. Write a program that asks the user for a weight in kilograms and converts it to pounds. 
# There are 2.2 pounds in a kilogram
Kg = float(input("Enter your weight in Kg:"))
##convert kg to pound
pound =(2.2 * Kg) 
print("Your weight in pound is",pound)

# Write a program that asks the user to enter three numbers (use three separate input statements).
# Create variables called total and average that hold the sum and average of the three numbers
# and print out the values of total and average.
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
total = num_1 + num_2 + num_3
average = total / 3

print("The total and average of the number entered are",total, "and",average,"respectively")

#A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
#the percent tip they want to leave. Then print both the tip amount and the total bill with the tip included

meal_price = int(input("Enter the price of the meal: "))
percent_tip = float(input("Enter the percent tip you want: "))

tip_amount = (percent_tip/100) * meal_price
total_bill = tip_amount + meal_price

print(f"The tip amount is {tip_amount} and the total bill inclusive of the tip is  {total_bill}")