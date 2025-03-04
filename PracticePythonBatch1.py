#Prog1- Program that prints bigger number
#option1
num= list(map(int,input("Enter numbers separated with commas: ").split(",")))
max_value= max(num)

print(f"The user's input:{num}")
print(f"The The highest number is:{max_value}")
#option2
num1= int(input("Enter your first number: "))
num2= int(input("Enter your second number: "))
maximum= max(num1,num2)

print(f"The user's input: {num1},{num2}")
print(f"The highest number is: {maximum}")

#Prog2- program that prints EQUAL when numbers are the same
#option 1
number_1= int(input("Enter a first number: "))
number_2= int(input("Enter a second number: "))
if number_1 == number_2:
    print("Equal")
else:
    print("Not Equal")

#Prog3- print the sum of the two numbers
number1= int(input("Enter a number: "))
number2= int(input("Enter a number "))
sum1= number1 + number2
print(f"The sum is: {sum1}")

#prog4- prints the product of two numbers
input1= int(input("Enter a number: "))
input2= int(input("Enter a number: "))
product= input1 * input2
print(f"The product is: {product}")

#prog5- prints the quotient of two numbers
try:
    num_1= float(input("Enter a number: "))
    num_2= float(input("Enter a number: "))
    quotient= num_1/num_2
    print(f"The quotient is: {quotient}")
except ZeroDivisionError:
    print("Error")

#prog6- Print the result when the first number is raised to the second number.

first_num= int(input("Enter a number: "))
second_num= int(input("Enter a number: "))
exponent= first_num ** second_num
print(f"The result of {first_num} raised to the power of {second_num} is: {exponent}")

#prog7- Print the sum of all numbers
user_input= list(map(int,input("Input 10 numbers separated with commas to comput the sum: ").split(",")))
sum_1= sum(user_input)

print(f"The sum of 10 numbers is: {sum_1}")

#prog8- Prints how many are odd numbers
numbers= []
for i in range(10):
    user_1 = int(input(f"Enter input {i+1}: "))
    numbers.append(user_1)
odd_count= 0
for i in numbers:
    if i %2 != 0:
        odd_count += 1

print(f"Total of Odd: {odd_count}")

#prog9- Prints all the even numbers from 0 to 100
for i in range (0,102,2):
    print(i)

#prog10- Prints all the numbers from 0-100 except numbers ending in zero

for i in range (0,101):
    if i %10 != 0:
        print(i)