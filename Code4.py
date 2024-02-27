#!/bin/python3

#Exercise 1
'''
outfile = open("words.txt", "w") 
word = input("Enter the words you would like to save (type STOP to end)\n")

while word != "STOP":                                                       #Creating while loop that keeps asking for new word and saving it until STOP is typed
    outfile.write(word+"\n")
    word = input("")

print("The session has ended, the words is saved in the file words.txt")

outfile.close()

'''
#Exercise 2
'''
infile = open("words.txt", "r")
words = []

for word in infile:                                                         #Iterates words in file and saves them to a list
    words.append(word)
infile.close()

words.sort()                                                                #Sorting alphabetically and reversing the list
words.reverse()
outfile = open("words.txt", "w")                                            #Opening words.txt with write permission

for i in words:                                                             #Iterating each word in the list, and writes them into the words.txt again.
    outfile.write(i)
outfile.close()
print("The file has been sorted and reversed")
'''
#Exercise 3
'''
infile = open("ex5.acc", "r")
lists = []
clean_list = []

for i in infile:                                                            #Iterating lines in file and saving them to a list
    lists.append(i)
infile.close()

for i in lists:                                                             #Iterating list and saving words that are not in the clean_list list already
    if i not in clean_list:
        clean_list.append(i)
        
clean_list.sort()                                                           #Sorting list
outfile = open("clean.acc", "w")                

for i in clean_list:                                                        #Write list into file
    outfile.write(i)
outfile.close()
'''

#Exercise 4
'''
infile = open("ex5.acc", "r")
clean_list = []

for i in infile:                                                            #Iterating lines and saving to clean list
    clean_list.append(i)
infile.close()

clean_list.sort()                                                           #Sorting list   

for i in reversed(range(len(clean_list)-1)):                                #Iterates the clean_list and if a string at [i] position is the same as [i+1] then removes it from the list
    if clean_list[i] == clean_list[i+1]:
        clean_list.pop(i)

outfile = open("clean.acc", "w")

for i in clean_list:                                                        #Writes list into file
    outfile.write(i)
outfile.close()

'''
#Exercise 5 
'''
infile = open("clean.acc", "r")
acc_num = input("Enter the accession number you are looking for: ")
data = []

for line in infile:                                                         #Appending lines into list
    data.append(line[:-1])
infile.close

while acc_num != "STOP":                                                    #Creating while loop that keeps asking for new acc number, and prints if it is there or not.
    for i in data:
        if acc_num == i:
            print("The accession number you are looking for is in the file")
            acc_num = input("Enter the accession number you are looking for: ")
            break
    else: 
        acc_num = input("The accession number you are looking for is NOT in the file, enter a new one:\n")

print("The session has stopped")       
'''
#Exercise 6 THIS IS NOT CORRECT AT ALL, I WAS TRYING, BUT FAILED.
'''
infile = open("clean.acc", "r")
data = []

for line in infile:
    data.append(line[:-1])
infile.close

low = 1
high = len(data)

mid = int((high+low)/2)

for i in range(1, mid):
    if acc_num == i:
        print("")
    else:
        
'''

#Exercise 7

# a)
'''
import sys

low = int(sys.argv[1])                                                      #Inserted the sys.argv[1] and [2]
high = int(sys.argv[2])
middle = int((high+low)/2)

print("The middle of", low, "and", high, "is",  middle)
'''
# b)
'''
import sys

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = input("Enter filename: ")
try:
	infile = open(filename, "r")
except IOError:
	print("Can't open file:", filename)
	sys.exit(1)
    
negatives = 0

for line in infile:
    for i in range(len(line)):
        if line[i] == '-':
            negatives += 1
infile.close()

print("Count of negative numbers:", negatives)

'''

# Exercise 8
'''
import sys

if len(sys.argv) == 3:                                              #Opens file with sys
	filename = sys.argv[1]
else:
	filename = input("Enter filename: ")                            #If file not present, then ask for filename
try:
	infile = open(filename, "r")                                    #Opens file
except IOError:
	print("Can't open file:", filename)                             
	sys.exit(1)

col = int(sys.argv[2])                                              #Sys argument, to pick the coloumn
numberlist = list()

for line in infile:                                                 #iterates each line and splits them, and appends each number to the number list
    numbers = line.split()
    for num in numbers:
        numberlist.append(float(num))
infile.close

new = []
for i in range(col,len(numberlist),3):                              #iterates the numberlist and appends the desired coloumn into a new variable list.
    new.append(numberlist[i])

print(new)
print(len(new))
'''

#Exercise 9
'''
infile = open("ex1.dat", "r")

data = list()

for line in infile:                                                 #Saves the numbers into a list
    for num in line.split():
        data.append(num)

sum_col1 = 0                                                        #Sum of the coloumn variables
sum_col2 = 0
sum_col3 = 0

for i in range(0,len(data),3):                                      #3x loops that iterates the numbers in increments of 3, and adds the number to the sum_col variable
    sum_col1 += float(data[i])
for i in range(1,len(data),3):
    sum_col2 += float(data[i])
for i in range(2,len(data),3):
    sum_col3 += float(data[i])

print("Total sum of the coloumn 1: ", sum_col1, "coloumn 2: ", sum_col2, "coloumn 3: ", sum_col3)
'''

#Exercise 10, brain malfunction