#!/bin/python3

#Exercise 1
'''
num1 = int(input("Enter a number:\n"))
num2 = int(input("Enter another number:\n"))

print("The mean of ", num1, "and", num2, "is", int((num1+num2)/2))
'''
#Exercise 2
'''
import sys

infile = open('numbers.txt', 'r')
num1 = infile.readline()
num2 = infile.readline()
sys.stdout.write(num1+num2)
infile.close()
'''
#Exercise 3
'''
neg_num = 0
infile = open('ex1.dat', 'r')
for line in infile:
    for character in line:                                                              #For loop that iterates each charachter in each line, if "-" is present, add +1 to the neg_num
        if character == "-":
            neg_num += 1
infile.close()
print(neg_num)
'''
#Exercise 4 
'''
user = input("Write a temperature, in celcius or fahrenheit for conversion\n")
temp = user[:-1]                                                                        #Grabs the temperature "100C" = "100"
conv = user[-1]                                                                         #Grabs the last charactor "100C" = "C"
tempcon = None

if conv == "C":                                                                         #Creating IF statements to determine if C or F is present in the input line.
    tempcon = (int(temp) * (9/5) + 32)
    print(tempcon, "F")
elif conv == "F":
    tempcon = (int(temp) - 32) * 5/9
    print(tempcon, "C")
'''
#Exercise 5
'''
infile = open('orphans.sp', 'r')
outfile = open('accession.txt', 'w')
for line in infile:
    for character in line:
        if character == ">":
            acc = line.split(' ')[0]
            acc = acc + "\n"
            for line in acc:
                outfile.write(line)
infile.close()
'''

#Exercise 6
'''
file1 = input('Please, enter a filename: \n')                                       #Asking for two file inputs
file2 = input('Please, enter a filename: \n')

infile1 = open(file1, 'r')
infile2 = open(file2, 'r')
outfile = open('copy.txt', 'w')

for line in infile1:                                                                #For loop that iterates each line in file1 and saves it to the copy variable
    copy = line[:-1]
    for line in infile2:                                                            #for loop that iterates each line in file2 and merges it with the line from "copy" and writes it to the output file
        merge = copy + "    " + line[:-1] + "\n"
        outfile.write(merge)
'''

#Asking user for first file input
#Asking user for second file input

#Open file one 
#Open file two 
#creating new document for the copy

#iterates through each line in file one
    #save each line in a variable
    #iterate through each line in second file
        #create new variable with the line of file one and file two
        #write output into the new document

#Exercise 7 
'''
infile = open('dna.dat', 'r')
outfile = open('complement.txt', 'w')
complement = ""

for line in infile:
    for character in line:
        if character == "A":
            complement += "T"
        elif character == "T":
            complement += "A"
        elif character == "C":
            complement += "G"
        elif character == "G":
            complement += "C"
outfile.write(complement)
print(complement)
'''

#Exercise 8
'''
infile = open('dna.dat', 'r')
outfile = open('reverse.txt', 'w')
complement = ""

for line in infile:
    for character in line:
        if character == "A":
            complement += "T"
        elif character == "T":
            complement += "A"
        elif character == "C":
            complement += "G"
        elif character == "G":
            complement += "C"

reverse = complement[::-1]           
outfile.write(reverse)
print(reverse)
'''
#Exercise 9
'''
infile = open('dna.dat', 'r')
outfile = open('revdna.dat', 'w')
complement = ""

for line in infile:                                                                 #Creating a loop that iterates through each line in the file 
    for character in line:                                                          #Creating a loop that iterates through each charachter in each line 
        if character == "A":                                                        #Making IF statements, if A is present, an T will be added to the complement strand etc.
            complement += "T"
        elif character == "T":
            complement += "A"
        elif character == "C":
            complement += "G"
        elif character == "G":
            complement += "C"

reverse = complement[::-1]                                                          #Reversing the complement strand

for i in range(0,len(reverse),60):                                                  #for loop that takes the first 60 charachters, prints them and write them into the output file.
    reverse_new = reverse[i:i+60]
    print(reverse_new)
    outfile.write(reverse_new + "\n")
'''
#Exercise 10
'''
infile = open('dna.fsa', 'r')
outfile = open('complementstrand.fsa', 'w')
complement = ""
for line in infile:                                                                 #Iterating each line in file
    for character in line:                                                          #iterating each character in line
        if character == ">":                                                        #if > is present, we split the line and add "complement strand". This was a wierd way to do something real simple, as using next(infile).
            acc = line.split('\n')[0] + " ComplementStrand"                         
    else:
        for line in infile:                                                         #Making complement strand
            for character in line:
                if character == "A":
                    complement += "T"
                elif character == "T":
                    complement += "A"
                elif character == "C":
                    complement += "G"
                elif character == "G":
                    complement += "C"
reverse = complement[::-1]                                                          #reversing complement strand

outfile.write(acc + "\n")                                                           #Next few lines writes the complement strand to the output file
print(acc)
for i in range(0,len(reverse),60): 
    reverse_new = reverse[i:i+60]
    print(reverse_new)
    outfile.write(reverse_new + "\n")
'''

#Exercise 11
'''

infile = open('dna.fsa', 'r')                                                       #Opening file
next(infile)                                                                        #Skipping first line
A = 0
T = 0
C = 0
G = 0
for line in infile:                                                                 #Creating a loop that iterates each line in file
    for i in line:                                                                  #Creating a loop that iterates each character in each line
        if i == "A":    
            A += 1
        elif i == "T":
            T += 1
        elif i == "C":
            C += 1
        elif i == "G":
            G += 1
print("Amount of AT/GC content in DNA", "A:", A, "T:", T, "C:", C, "G:", G)
        
            

'''

