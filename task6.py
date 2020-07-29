# 1.

try:
    eval('6=7')
except SyntaxError:
    print("Error in Syntax")

# 2.

import sys
def checkFile(filename):
    try:
        with open(filename, 'r') as file:
            print("File Opened")
            file.close
            print("File Closed")
    except FileNotFoundError:
        filename = input("No such file exists.\nEnter filename again: ")
        checkFile(filename)

checkFile(sys.argv[1])

# 3.

def checkDigits(num):
    if not '.' in num:
        return len(num)
    return len(num[:num.index('.')])

var1 = input("Enter a number: ")

if checkDigits(var1) != 4:
    print("Please length is too short/long !!! Please provide only four digits.") 

# 4.

count = 0
while(True):
    try:
        username = input("Username: ")
        password = input("Password: ")
        repass = input("Re-Type Password: ")
        if password != repass:
            raise Exception
        else:
            break
    except:
        if count < 3:
            count+= 1
        else:
            print("Maximum Attempts Reached.")
            break

# 6.

try:
    with open("sample.txt", 'r') as file:
        for line in file:
            if len(line) % 2 == 0:
                print(line)
        file.close
except:
    print("File Error")