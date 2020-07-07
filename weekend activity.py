# 1. 
list1 = ['hello', 'world', 10, 20, 0.49, 11.99, 21.99, 11+2j, 50+100j, 'consult add']

# 2.
list2 = [1] * 5

# 3.
x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[-3:-1])
print(x[::2])
print(x[::-1])
print([x[5][5][0]])
print([])

# 4.
result1 = list(range(1000))
# print(result1)

# 5.
## Tuple is immutable, hence they cannot be changed once assigned. However, lists are mutable objects, which can be changed. So tuples are used where data is not to be changed on regular basis such as username, passwords.

# 6.
## if a number is divisible by 3 and multiple of 2, then combining both it would be divisible by 6
for i in range(1,100):
    if i%6==0:
        print(i)

# 7.
vowel = ['a', 'e', 'i', 'o', 'u']
var1 = "hello world"
print(var1[::-1])
for i in vowel:
    k = var1.find(i)
    if k!=-1:
        print(i, k)

# 8.
var2 = "hello my name is Abcde"
var2 = var2.split(" ")
for i in var2:
    if len(i)%2==0:
        print(i)

# 9.
x = [1,2,3,4,5,6,7,8,9,-1]
target = 8
result2 = set()
for i in x:
    rsum = target - i
    if rsum in x[i+1:] or rsum in x[0:i-1]:
        result2.add((i, rsum)) if i<rsum else result2.add((rsum,i))
print(list(result2))

# 10.
even_list = []
odd_list = []

num = int(input("Enter number between 1 - 50: "))
while(len(even_list)<=5 and len(odd_list)<=5):
    even_list.append(num) if num%2==0 else odd_list.append(num)
    num = int(input("Enter number between 1 - 50: "))
    
print(sum(even_list), max(even_list))
print(sum(odd_list), max(odd_list))

# 11.
var3 = "12abcbacbaba344ab"
result3 = {}
for i in var3:
    if not i.isdigit():
        var3[i]+=1

