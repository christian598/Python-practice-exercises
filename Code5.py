#!/usr/bin/env python3

#Exercise 1

import re
user = input("Enter something\n")

if re.search(r'^[-]?\d+[^\w][.]?[^+-]\d+', user):
    print("The string is a number")
else:
    print("The string is not a number")


#Exercie 2


import re

infile = open("sprot1.dat", "r")
outfile = open("sprot1.fsa", "w")

acc = ""
ID = ""
sequence = ""
aa_length = None

for line in infile:
    if line.startswith('AC'):
        acc = re.search(r'^AC\s+(\w+);', line).group(1)
    if line.startswith('ID'):
        ID = re.search(r'^ID\s+(\w+)', line).group(1)
    if line.startswith('   '):
        sequence += line

sequence = sequence.replace(" ", "")      

print("Accession:", acc, "\n", "ID:", ID, "\n", "Sequence:", sequence)


#Exercise 3

import re
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

outfile = open('complementstrand.fsa', 'w')

dna = ""
complement = ""
translationTable = str.maketrans('ATCG', 'TAGC')                        #Translation table

for line in infile:                                                     #For loop finds the line that starts with '>', and while the string is empty, outwrite the variable complement.
    if line.startswith('>'):
        if complement != "": 
            outfile.write(complement[::-1])
            complement = ""
        outfile.write("\n"+line[:-1])
    else:                                                               #If '>' is not present, translate the line and add to the complement string.
        complement += line.translate(translationTable)


#Exercise 4,5, 6

import re

infile = open("data1.gb", "r")

acc = ""
deff = ""
organism = ""
medline = list()

for line in infile:
    if line.startswith('ACCESSION'):
        acc = re.search(r'^\w+\s+(\w+)', line).group(1)
    if line.startswith('DEFINITION'):
        deff = re.search(r'^\w+\s+(.+)', line).group(1)
    if line.startswith('  ORGANISM'):
        organism = re.search(r'^\s+\w+\s+(.+)', line).group(1)
    if line.startswith('  MEDLINE'):
        medline.append(re.search(r'^\s+\w+\s+(\d+)', line).group(1))
        
print(acc)
print(deff)
print(organism)
print(medline)


#Exercise 7-9 stateful parsing

import re

infile = open("data1.gb", "r")

info = list()
acc = ""
deff = ""
organism = ""
medline = list()
(data, seqflag) = ("", False)

for line in infile:
    if line.startswith('ACCESSION'):
        acc = re.search(r'^\w+\s+(\w+)', line).group(1)
    if line.startswith('DEFINITION'):
        deff = re.search(r'^\w+\s+(.+)', line).group(1)
    if line.startswith('  ORGANISM'):
        organism = re.search(r'^\s+\w+\s+(.+)', line).group(1)
    if line.startswith('  MEDLINE'):
        medline.append(re.search(r'^\s+\w+\s+(\d+)', line).group(1))
        
#Stateful parsing, finding the translation sequence
    if re.search(r'^\s+\w+.?\w+\s+\d+', line):
        seqflag = False
    if seqflag:
        data += line
    if line.startswith('/translation', 21, 34):
        data += line
        seqflag = True
data = data.replace(" ", "")
data = data.strip()

print(acc)
print(deff)
print(organism)
print(medline)
print(data)


#Exercise 8

import re

infile = open("data4.gb", "r")

info = list()
acc = ""
deff = ""
organism = ""
medline = list()
(data, seqflag) = ("", False)
(dna, flag) = ("", False)

for line in infile:
    if line.startswith('ACCESSION'):
        acc = re.search(r'^\w+\s+(\w+)', line).group(1)
    if line.startswith('DEFINITION'):
        deff = re.search(r'^\w+\s+(.+)', line).group(1)
    if line.startswith('  ORGANISM'):
        organism = re.search(r'^\s+\w+\s+(.+)', line).group(1)
    if line.startswith('  MEDLINE'):
        medline.append(re.search(r'^\s+\w+\s+(\d+)', line).group(1))
        
#Stateful parsing, finding the translation sequence
    if re.search(r'^\s+\w+.?\w+\s+.*\w*\d+', line):
        seqflag = False
    if seqflag:
        data += line
    if line.startswith('/translation', 21, 34):
        data += line
        seqflag = True
#Stateful parsing, finding the DNA sequence    
    if line[:-1] == "//":
        flag = False
    if flag:
        dna += line[10:-1]
    if line[:6] == "ORIGIN":
        flag = True        

#Removing space and newline from the sequences
data = data.replace(" ", "")
data = data.strip()
dna = dna.replace(' ', '')
dna = dna.strip()

print(acc)
print(deff)
print(organism)
print(medline)
print(data)
print(dna)

#Exercise 9

import re

infile = open("data1.gb", "r")

info = list()
acc = ""
deff = ""
organism = ""
medline = list()
(data, seqflag) = ("", False)
(dna, flag) = ("", False)

#Finding Accession, definition, organism and medlines, using RegularExpression
for line in infile:
    if line.startswith('ACCESSION'):
        acc = re.search(r'^\w+\s+(\w+)', line).group(1)
    if line.startswith('DEFINITION'):
        deff = re.search(r'^\w+\s+(.+)', line).group(1)
    if line.startswith('  ORGANISM'):
        organism = re.search(r'^\s+\w+\s+(.+)', line).group(1)
    if line.startswith('  MEDLINE'):
        medline.append(re.search(r'^\s+\w+\s+(\d+)', line).group(1))
        
#Stateful parsing, finding the translation sequence
    if re.search(r'^\s+\w+.?\w+\s+.*\w*\d+', line):                             #Finding line that starts with space, some word and then a space with some digits.
        seqflag = False
    if seqflag:
        data += line
    if line.startswith('/translation', 21, 34):                                 #Finding the line that starts with "/translation" at position 21,34 in the line.
        data += line                                                    
        seqflag = True
#Stateful parsing, finding the DNA sequence    
    if line[:-1] == "//":                                                       #If line starts with "//" at position[:-1], set flag as False
        flag = False
    if flag:                                                                    #While the flag is true, add the line to dna.
        dna += line[10:-1]
    if line[:6] == "ORIGIN":                                                    #If "ORIGIN" is present at position[:6], set flag as True
        flag = True        

#Removing space and newline from the sequences
data = data.replace(" ", "")
data = data.strip()
dna = dna.replace(' ', '')
dna = dna.strip()




print(acc)
print(deff)
print(organism)
print(medline)
print(data)
print(dna)