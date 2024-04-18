print("hello world!")
# fast easy comment
'alternative to comment above'
'''
use this for longer block of comments
it can easily comment several lines
'''

# Variables
'''
Drawn on board
int x = 100 (Java, must declare data type)
x = 100
can put any value in a variable
the value determines the data type
'''
x = 100
y = 5.5
x = "hello"
x = [1,2,3]

# Math operations
# result is always a float
intx = 100
inty = 10
result = intx/inty
print(result)
# cast result to int
result = int(result)
print(result)

# and alternative is floor division which will discard any remainder
result = intx // inty
print(result)

# math module built in functions
min_val = min(10, 1)
print(min_val)
raised = pow(2,4)
print(raised)
# faster way
raised = 2**4
print(raised)

# if statements and concatenating output
# blocks of code are not put in curly brackets
# indentation is required
x = -1
y = 1
if x < 0:
    print('x is less than 0')
    x += 1

if x < 0 and y > 0:
    print('x and y within range')

if x < 0 or y < 0:
    print('x or y less than 0')

if x < 0:
    print('the value of x is', x, 'and it is less than 0')
elif x > 0:
    print('x is greater than 0')
else:
    print('x is 0')

# Loops
nums = [10,20,30,40,50]   
for i in range(len(nums)):
    print(nums[i])

for val in nums:
    val += 5
    print(val)
print(nums)

for i, val in enumerate(nums):
    print("i is", i, "and val is", val)

dogs=["boomer", "rocky", "daisy"]
for i in range(len(dogs)):
    print(dogs[i])

for val in dogs:
    print(val)
print(dogs)

for i, val in enumerate(dogs):
    print("i is", i, "and val is", val)

numbers=[1, 2, 3, 4]
sum = 0
for val in numbers:
    sum += val
print("sum of numbers is",sum)
print(f"the sum of numbers is {sum}")

def hello(name="friend"):
    print("hello!",name)
hello("Bob")
hello()

fname = 'Ria'
lname = "Shaji"

print(fname)
print(lname)

print("She's a great dancer.")

fulLname = fname + lname
print(fulLname)

first_Char = fname[0]
print(first_Char)
print(fname[-1])

name_3 = fname * 3
print(name_3)

full_name = "Ria Shaji"
fname = full_name[0:8]
print(fname)

platform_computing = "platform.computing"
platform = platform_computing[0:8]
computing = platform_computing[9:18]
print(platform)
print(computing)

nums = [0,3,8,5,4]
temp = nums[2]
nums[2] = nums[4]
nums[4] = temp
print(nums)
