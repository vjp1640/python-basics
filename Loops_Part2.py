#While loops in Python

#Simple while loop
x = 0
while x < 5:
	print(f'Current value of x is {x}')
	x = x + 1

#can also write x = x + 1 as x += 1

#while loop with else
x = 0
while x < 5:
	print(f'Current value of x is {x}')
	x += 1
else:
	print(f'X is not less than 5')

#break, continue and pass add additional functionality to loops
#pass - place holder, skip 
#continue - go to the top of the closest enclosing loop
#break - break out of the current closest enclosing loop 

#example for continue
for letter in 'hello':
	if letter == 'l':
		continue
	print(letter)
#Output:
#h	
#e
#o	

	
#example for break
for letter in 'hello':
	if letter == 'l':
		break
	print(letter)
#Output:
#h	
#e

#Break for while loops
x = 0
while x < 5:
	if x == 3:
		break
	print(f'Current value of x is {x}')
	x += 1
else:
	print(f'X is not less than 5')
#Output:	
# Current value of x is 0
# Current value of x is 1
# Current value of x is 2
# Current value of x is 3
# Current value of x is 4
# X is not less than 5

#simple inbuilt functions

#range
for num in range(10, 20, 2):
	print(num)
#Output:	
# 10
# 12
# 14
# 16
# 18

#enumerate
for item in enumerate('word'):
	print(item)
#Output
# (0, 'w')
# (1, 'o')
# (2, 'r')
# (3, 'd')

for index,letter in enumerate('word'):
	print(index)
	print(letter)
	print('\n')
#Output
# 0
# w


# 1
# o


# 2
# r


# 3
# d


#zip - concatenate list in python
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c']
zip(mylist1, mylist2)
for item in zip(mylist1, mylist2):
	print(item)
#Output
# (1, 'a')
# (2, 'b')
# (3, 'c')	

list(zip(mylist1, mylist2))
#Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c']
zip(mylist1, mylist2)
for a,b in zip(mylist1, mylist2):
	print(a)
#Output:
# 1
# 2
# 3

#in - checks ifthe item is present in the list, dictionary, logical output
'x' in ['x','y','z']
#Output:
# True

d = {'a':1}
1 in d.values()
#Output:
# True

1 in d.keys()
#Output:
# False

#import - import libraries 
from random import shuffle

rand1 = shuffle(mylist1)
rand1
type(rand1)
#Output:
# NoneType

from random import randint
rand1 = randint(0,100)
rand1
#Output:
# 77

result1 = input('Enter a number here: ')
#Output:
# Enter a number here: 10

result1
#Output:
# '10'

type(result1)
#Output:
# str

int(result1)
#Output:
# 10


#Difference between .append() and for-in
mylist1=[]
mylist = 'hello'
for letter in mylist:
	mylist1.append(letter)
mylist1
#Output:
# ['h', 'e', 'l', 'l', 'o']


mylist1=[]
mylist1 = [letter for letter in mylist]
mylist1
#Output:
# ['h', 'e', 'l', 'l', 'o']


word1 = [word for word in 'word']
word1
#Output:
# ['w', 'o', 'r', 'd']


list1=[]
list1 = [num for num in range(0,11)]
list1
#Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


list1=[]
list1 = [num**2 for num in range(0,11)]
list1
#Output:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list1=[]
list1 = [num**2 for num in range(0,11) if num%2==1]
list1
#Output:
# [1, 9, 25, 49, 81]


cel = [0, 10, 20, 35.5, 70] 
farhen = [(9/5*temp+32) for temp in cel]
farhen
#Output:
# [32.0, 50.0, 68.0, 95.9, 158.0]


result = [x if x%2==0 else 'odd' for x in range(0,10)]
result
#Output:
# [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']


list1=[]
for x in [1,2,3]:
	for y in[4,5,6]:
		list1.append(x*y)
list1
#Output:
# [4, 5, 6, 8, 10, 12, 12, 15, 18]


list1=[]
for x in [1,2,3]:
	for y in[10,100,1000]:
		list1.append(x*y)
list1
#Output:
# [10, 100, 1000, 20, 200, 2000, 30, 300, 3000]


list1=[]
list1 = [x*y for x in [1,2,3] for y in [10,100,1000]]
list1
#Output:
# [10, 100, 1000, 20, 200, 2000, 30, 300, 3000]


