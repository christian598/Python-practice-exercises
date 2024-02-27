#!/usr/bin/env python3

#1 Reads file and prints each line in the file
'''
with open ('ex1.acc', 'r') as infile:
    for line in infile:
        print(line)
print('Now done with the file')
'''
#2 Make the program ask for a filename (the input file in the following exercises), and display the file on the screen. A bit more like cat.

'''
filename = input('Please, enter a filename: \n')

with open (filename, 'r') as infile:
    for line in infile:
        print(line)
print('Now done with the file')
'''

#3 Construct a program that counts the number of lines in the input file, and displays the result. Try it with the file ex1.dat. There are 1675 lines.

'''
result = 0

with open ('ex1.acc', 'r') as infile:
    for line in infile:
        result += 1
print("Total lines in the file: ", result)

'''

#4 Construct three files from ex1.dat using unix commands
#cut -f1 ex1.dat > col1
#cut -f2 ex1.dat > col2
#cut -f3 ex1.dat > col3

#Python program that sums up the numbers of each file and displays them

'''
result = 0
filename = input('Please, enter a filename: \n')

with open (filename, 'r') as infile:
    for number in infile:
        result += float(number)
print("Total sum of the coloumn: ", result)
'''

#5 Calculates the mean value
'''
lines = 0
result = 0
filename = input('Please, enter a filename: \n')

with open (filename, 'r') as infile:
    for number in infile:
        result += float(number)
        lines += 1
print("Total sum of the coloumn: ", result)
print("Mean value of the coloumn: ", result/lines)
'''

#6 counts the number of positive and negative numbers and zeros
'''
pos = 0
neg = 0
zero = 0

filename = input('Please, enter a filename: \n')

with open (filename, 'r') as infile:
    for number in infile:
        num = float(number)
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero +=1
print("Total positive numbers: ", pos)
print("Total negative numbers: ", neg)
print("Total zeros: ", zero)
'''

#7 finds the maximum number in a column

'''

maxi = 0

filename = input('Please, enter a filename: \n')

with open (filename, 'r') as infile:
    for number in infile:
        num = float(number)
        if num > maxi:
            maxi = num
print("The maximum value is: ", maxi)

'''

#8 finds the minimum number in a column 
'''
mini = 0
filename = input('Please, enter a filename: \n')

with open (filename, 'r') as infile:
    for number in infile:
        num = float(number)
        if num < mini:
            mini = num
print("The minimum value is: ", mini)

'''

#9 calculate the sum, the number of lines, the mean value, the number of positive, negative and zero numbers, the maximum and the minimum value. Only reads the file once
'''
lines = 0
result = 0
pos = 0
neg = 0
zero = 0
maxi = 0
mini = 0

filename = input('Please, enter a filename: \n')

with open (filename, 'r') as infile:
    for number in infile:
        result += float(number)                                 #Total sum of coloumn
        lines += 1                                              #Number of lines
        num = float(number)
        
        #Calculate number of negative, postive and zeros
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero +=1
            
        #Calculate maximum and minimum
        if num > maxi:
            maxi = num
        elif num < mini:
            mini = num
        
        #Printing results
print("Total lines in the file: ", lines)
print("Total sum of the coloumn: ", result)
print("Mean value of the coloumn: ", result/lines)
print("Total positive numbers: ", pos)
print("Total negative numbers: ", neg)
print("Total zeros: ", zero)
print("The maximum value is: ", maxi)
print("The minimum value is: ", mini)
'''

#10 Number guesser

import random

num = random.randint(1,10)
user = 0

while num != user:
    num = random.randint(1,10)
    user = int(input('Enter a number:\n'))
    print(num)
    
    if num == user:
        break
    else:
        while num != user:
        
            user2 = input("Is the number higher or lower?\n")
        
            if user2 == "higher":
                num = random.randint((num+1), 10)
                print(num)
            elif user2 == "lower":
                num = random.randint(1, (num-1))
                print(num)
            else: 
                print("Error: type: higher or lower")
print("WOOOOO! I guessed it")
        
