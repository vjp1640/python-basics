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
