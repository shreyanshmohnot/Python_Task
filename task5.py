# 1.

var1 = [21, 35]
remove_7div = lambda x:x%7==0
result1 = list(filter(remove_7div, filter(remove_3div, var1)))

# 2.

def multiply(x):
    return x*x

result2 = map(multiply, range(10))

# 3.

var2 = "hELLo WorLD"
result3 = [x for x in var2 if x.isupper()]

# 4.

Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
result4 = dict(zip(Student, capital))

# 6.

str1 = "Consultadd Training"

def reverse_string(x):
    for i in range(len(x) - 1, -1, -1):
        yield x[i]

for r in reverse_string(str1):
    print(r)
    
# 7.

def make_pretty(func):
    def inner():
        print("Pretty printing")
        func()
    return inner

@make_pretty
def not_pretty():
    print("Not pretty printing")

not_pretty()

# 8.

'''
Front End - React.js, Angular JS, Bootstrap, Javascript, AJAX
Facebook, Instagram, Shopify, Slack
'''