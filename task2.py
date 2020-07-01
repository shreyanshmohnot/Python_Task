# 1.

x = 25

if x%3 == 0:
    print("Consultadd")

if x%5 == 0:
    print("c")

# if a number is divisible by 3 & 5, it would be divisble by 15.
if x%15 == 0:
    print("Consultadd Python Training")

# 2.

print("1. Addition \n2. Subtration \n3. Division \n4. Multiplication \n5. Average")
var1 = eval(input("Please enter you input: "))

if var1 == 5:
# enter two inputs spaced by comma - ,
    first, second, first1, second2 = eval(input("Enter four numbers(separated by ,): "))
    avg = (first+second+first1+second2)/4
    print(avg) if avg>0 else print("Zsa")

else:
# enter two inputs spaced by comma - ,
    first, second = eval(input("Enter two numbers(separated by ,): "))
    ans = {1: first+second,
           2: first-second,
           3: first/second,
           4: first*second}
    print(ans.get(var1)) if ans.get(var1) > 0 else print("Zsa")

# 3.

age = 38
if age >= 11:
    print("You are eligible to see the Football match.")
    if age <= 20 or age >= 60:
        print("Ticket price is $12")
    else:
        print("Ticket price is $20")
else:
    print("You're not eligible to buy a ticket.")

# 4.

while True:
    num1 = eval(input("Enter a number: "))
    if num1 < 0:
        print("It's Over")
        break
    else:
        print("Good Going")
        continue

# 5.

for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

# 6.

#Part 1 - error, because it is not iterable. just a constant integer

#Part 2 - 
# 0
# error
# 1
# error
# 2

#Part 3 - 
# 0
# 1
# 2
# 3
# 4

# 7.

for i in range(0,6):
# no need for second comparsion because the range stops before 6
    if i == 3 or i == 6:
        continue
    print(i)

# 8.

letters = digits = 0

str1 = "consul12"

for s in str1:
    if s.isdigit():
        digits += 1
    if s.isalpha():
        letters += 1

print("Letters ", letters)
print("Digits ", digits)

# 9.

# Part 1 - 
lucky_number = 10
answer = eval(input("Guess Lucky Number: ")) != lucky_number
while answer:
    print()

# Part 2 -
lucky_number = 10
answer = int(input("Guess Lucky Number: ")) != lucky_number
while answer and input("Do you want to guess again: ") == "yes":
    number = int(input("Guess again: "))
    answer = number != lucky_number

# 10.

lucky_number = 10
counter = 1
while counter <= 5:
    num = int(input("Type in the " + str(counter) + " number: "))
    counter += 1
    if num == lucky_number:
        print("Good guess!")
    else:
        print("Try again!")
print("Game over!")

# 11.

lucky_number = 10
counter = 1
while counter <= 5:
    num = input("Type in the " + str(counter) + " number: ")
    if not num:
        print("Sorry but that was not very successful")
        continue
    counter += 1
    if int(num) == lucky_number:
        print("Good guess!")
        break
    else:
        print("Try again!")
print("Game over!")
