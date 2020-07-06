# 1. 
list1 = ['hello', 'world', 10, 20, 0.49, 11.99, 21.99, 11+2j, 50+100j, 'consult add']

# 2.
list2 = [1] * 5

# 3.
add = sum(list2)
mul = 1
for i in list2:
    mul *= i

# 4.
print(min(list2))
print(max(list2))

# 5.
pre_def = [int(i*i/7) for i in range(1,50,5)]
for i in pre_def:
    if i%2 == 0:
        pre_def.remove(i)

# 6.
sq_list = [i*i for i in range(31)]
result1 = sq_list[:5]
result1.extend(sq_list[-5:])

# 7.
sdata = [[1,3,5,7,9,10],[2,4,6,8]]
sdata[0].pop()
sdata[0].extend(sdata[1])
print(sdata[0])

# 8.
ndict = {}
a = {1:10, 2:20}
b = {3:30, 4:40}
ndict.update(a)
ndict.update(b)
print(ndict)

# 9.
n = 5
result2 = {}
for i in range(1, n+1):
    result2[i]=i*i

# 10.
input_seq = input("Enter numbers separated by comma: ").split(',')
print(input_seq)
print(tuple(input_seq))