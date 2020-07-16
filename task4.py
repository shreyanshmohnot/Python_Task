# 1.

def reverseSTR(sdata):
    return sdata[::-1]

sdata = "FDGabcd"
# print(reverseSTR(sdata))

# 2.

def calculateSTR(sdata):
    res = {"upper":0, "lower":0}
    for i in sdata:
        if i.isupper():
            res["upper"] += 1 
        elif i.islower():
            res["lower"] += 1
    return res

result1 = calculateSTR(sdata)

# 3.

var1 = [1,2,3,4,5,3,7]

def uniqueItems(var):
    return list(set(var))

result2 = uniqueItems(var1)

# 4.
'''
var2 = input("Enter string hyphen separated: ").split("-")
var2.sort()
print("-".join(var2))
'''
# 5.

lines = []
'''
while True:
    ##empty input breaks the loop
    line = input("Enter Input: ")
    if not line:
        break
    lines.append(line.upper())

print("\n".join(lines))
'''
# 6.

def computeSUM(var1, var2):
    return int(var1) + int(var2)
'''
varFirst = input("Enter first number: ")
varSecond = input("Enter second number: ")
print(computeSUM(varFirst, varFSecond))
'''
# 7.

def printMaxSTR(lines):
    if len(lines[0]) == len(lines[1]):
        return lines[0]+"\n"+lines[1]
    elif len(lines[0]) < len(lines[1]):
        return lines[1]
    else:
        return lines[0]

'''
lines = [input("Enter String: ").rstrip() for i in range(2)]
print(printMaxSTR(lines))
'''
# 8.

def generateSquares(i):
    return 