#!/usr/bin/env python3

#Exercise 1

import sys

if len(sys.argv) == 2:                                                  #Code for opening the file, as a sys argument. If that fails, ask user for filename.
	filename = sys.argv[1]
else:
	filename = input("Enter filename: ")
try:
	infile = open(filename, "r")
except IOError:
	print("Can't open file:", filename)
	sys.exit(1)
    
mean = list()

for line in infile:                                                     #Saving data in a list of lists
    mean += [line.split()]   

for row in range(len(mean)):                                            #Iterating each row
    for column in range(1, len(mean[row])):                             #Iterating each column, excluding the first position, which is the acc num
        mean[row][column] = float(mean[row][column])                    #Making each num into a float
    mean[row][1] = (sum(mean[row][1:])/(len(mean[row])-1))              #Calculating the mean of each num on in the list of lists and saving it at pos [1]
    mean[row][2:] = []                                                  #Removing the rest the numbers in the list, so we have (Accession, Mean) in each list

for i in range(len(mean)):                                              #Printing each list one at a time, with Acc num and Average.    
    print("Accession:", mean[i][0], "Average:", mean[i][1])


#Exercise 2

import sys

if len(sys.argv) == 2:                                                  #Code for opening the file, as a sys argument. If that fails, ask user for filename.
	filename = sys.argv[1]
else:
	filename = input("Enter filename: ")
try:
	infile = open(filename, "r")
except IOError:
	print("Can't open file:", filename)
	sys.exit(1)
    
def transpose(matrix):                                                                      #Making function for transposing the matrix
    trans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]     #Transpose the matrix
    for num in range(len(trans)):                                                           #Prints the matrix once at a time (list once at a time)
        print(trans[num])


matrix = list()
    
for line in infile:                                                                         #Saving matrix into a list of lists
    matrix += [line.split()]

for i in matrix:                                                                            #Printing both matrix
    print(i)
print("------------------------")
print(transpose(matrix))

