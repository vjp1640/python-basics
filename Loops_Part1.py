
#Loops in Python

#If and else if loops

# Write a program that prints the integers from 1 to 30. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

num1 = range(1,31)
for num in num1:
    if num%3==0 and num%5!=0:
        print('Fizz')
    elif num%5==0 and num%3!=0:
        print('Buzz')
    elif num%3==0 and num%5==0:
        print('FizzBuzz')
    else:
        print(num)

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz


#For loops for lists, strings, tuples and dictionaries

#here defining mylist is important, num can be undefined. you can use any word to index iterations
mylist = [1, 2, 3, 4, 5]
for num in mylist:
	print(num)

#the list can be defined in the for loop itself
for letter in [1, 2, 3, 4, 5]:
	print(letter)


#I have used the word jelly instead of num, still works the same
mylist = [1, 2, 3, 4, 5]
for jelly in mylist:
	print(jelly)


#printing hello for each iteration
mylist = [1, 2, 3, 4, 5]
for jelly in mylist:
	print('hello')
	
#adding an if statement in the for loop
#print the number only if it is even
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
	if num % 2 == 0:
		print(num)


#adding an if statement in the for loop
#print all numbers but mention if it is an odd number
#indentation is important in python

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
	if num % 2 == 0:
		print(num)
	else:
		print(f'Odd number:{num}')
		

#sum of numbers in a list
#printing the total sum directly and not the sum at each iteration

num_sum = 0
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
	num_sum = num_sum + num
print (num_sum)


#sum of numbers in a list
#printing the sum at each iteration

num_sum = 0
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
	num_sum = num_sum + num
	print (num_sum)


#sum of even numbers in a list
#skip the number from the sum if it is odd
num_sum = 0
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
	if num % 2 == 0:
		num_sum = num_sum + num
		print (f'The iterative sum of even numbers is {num_sum}')
	else:
		print(f'Skipped the number {num} as it is odd')

#Output for thr above code:
#Skipped the number 1 as it is odd
#The iterative sum of even numbers is 2
#Skipped the number 3 as it is odd
#The iterative sum of even numbers is 6
#Skipped the number 5 as it is odd
#The iterative sum of even numbers is 12
#Skipped the number 7 as it is odd
#The iterative sum of even numbers is 20
#Skipped the number 9 as it is odd
#The iterative sum of even numbers is 30

###
#Strings are ordered so we can iterate using strings as well
mystring = 'Hello world'
for letter in mystring:
	print(letter)

#we need not define the iterative variable or the string 
for letter in 'Hello':
	print(letter)
	
#The indexing variable can be undefined
for abc in 'Hello':
	print(abc)

	
#You can use _ sign instead of the indexing variable when you do not need the indexing var further in the code
for _ in 'Hello':
	print('Hi')

#Same logic for tuples
tup = (1, 2, 3)
for i in tup:
	print(i)
		
#Unpacking of tuples for for loops
mylist = [(1,2), (3,4), (5,6)]
len(mylist)
for tup1 in mylist:
	print(tup1)

#Printing all the objects in each tuple
for (a,b) in mylist:
	print(a)
	print(b)

#Printing just the first object in each tuple
for (a,b) in mylist:
	print(a)

for (a,b) in mylist:
	print(b)

#() for the indexing of tuples is also not required
for a,b in mylist:
	print(a)

	
#Iterating through dictionaries
dict1 = {'a':1, 'b':2, 'c':3}
for alph in dict1:
	print(alph)
#This will print the key items only and not the items associated with the key.
#Output will be:
#a
#b
#c

dict1 = {'a':1, 'b':2, 'c':3}
for alph in dict1.items():
	print(alph)
#This is going to print both the key and the items
#Output will be as follows
#('a', 1)
#('b', 2)
#('c', 3)	

#just want to print the items/values. USe tuple unpacking again
dict1 = {'a':1, 'b':2, 'c':3}
for key,value in dict1.items():
	print(value)

for key,value in dict1.values():
	print(value)

#List comrehensions
#For loops with .append()
mylist1=[]
mylist = 'hello'
for letter in mylist:
	mylist1.append(letter)
mylist1
# ['h', 'e', 'l', 'l', 'o']

#Alternative way of doing the above thing
mylist1=[]
mylist1 = [letter for letter in mylist]
mylist1
# ['h', 'e', 'l', 'l', 'o']

word1 = [word for word in 'word']
word1
# ['w', 'o', 'r', 'd']

list1=[]
list1 = [num for num in range(0,11)]
list1
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#You can perform operations for the items in the list
#Get the squares of the numbers in the original list
list1=[]
list1 = [num**2 for num in range(0,11)]
list1
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#Will give square of only odd numbers
list1=[]
list1 = [num**2 for num in range(0,11) if num%2==1]
list1

#Celsius to farhenheight
cel = [0, 10, 20, 35.5, 70] 
farhen = [(9/5*temp+32) for temp in cel]
farhen

#if else in for
result = [x if x%2==0 else 'odd' for x in range(0,10)]
result
# [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']

#Nested for loops
list1=[]
for x in [1,2,3]:
	for y in[10,100,1000]:
		list1.append(x*y)
list1
		
#[10, 100, 1000, 20, 200, 2000, 30, 300, 3000]

#Compact version with less readability
list1=[]
list1 = [x*y for x in [1,2,3] for y in [10,100,1000]]
list1
#[10, 100, 1000, 20, 200, 2000, 30, 300, 3000]


#Coding exercises
###
### Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0]=='s':
        print(word)
	# start
	# s
	# sentence
	
for word in st.split():
    if word[0].lower()=='s' and len(word)>1:
        print(word)

# start
# sentence

###
### **Use range() to print all the even numbers from 0 to 10.**
for num in range(0,11):
    if num%2==0:
        print(num)
# 0
# 2
# 4
# 6
# 8
#10

###
### Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
list1 = [num for num in range(1,51) if num%3==0] 
list1
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

###
###**Go through the string below and if the length of a word is even print "even!"**
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print('even!')
# even!
# even!
# even!
# even!
# even!
# even!
# even!
# even!
# even!


###
### Write a program that prints the integers from 1 to 30. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

num1 = range(1,31)
for num in num1:
    if num%3==0 and num%5!=0:
        print('Fizz')
    elif num%5==0 and num%3!=0:
        print('Buzz')
    elif num%3==0 and num%5==0:
        print('FizzBuzz')
    else:
        print(num)

#easier way, fizzbuzz condition first followed by the individal ones

num1 = range(1,31)
for num in num1:
    if num%3==0 and num%5==0::
        print('FizzBuzz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0:
        print('Fizz')
    else:
        print(num)
		
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz

###
#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
list1 = [letter[0] for letter in st.split()]
list1

#['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']

