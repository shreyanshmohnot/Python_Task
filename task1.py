# 1.
i, j, k = 2, "Three", 4.99

# 2.
a, b = 1+32j, 11
b, a = a, b

# 3.
# third variable
var1, var2 = 5, 10
result = var1
var1 = var2
var2 = result

# 1-liner
var1, var2 = var2, var1

# 4.
ab = input()
print(ab)
print ab

# 5.
z = sum(map(int, input("Enter 2 numbers betwenn 1-10: ").split()))
z += 30
print(z)

# 6.
var = "Hello"
print("The input value data type is", type(var).__name__)

# 7.
# Yes, it will change the value, because python considers recent assignment and overwrites any particular previous values.