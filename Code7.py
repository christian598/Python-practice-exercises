#!/usr/bin/env python3

#Exercise 1
'''
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

def complement(dna):                                                    #Simple function that makes the reverse complement strand. 
    comp = ""
    translationTable = str.maketrans('ATCG', 'TAGC')
    comp += dna.translate(translationTable)
    comp = comp[::-1]
    return comp

dna = ""
comp = ""
for line in infile:                                                     #Loop that reads a line, calls the function and get the reverse complement and outfile writes it.
    if line.startswith('>'):
        if comp != "": 
            outfile.write(complement(comp))
            comp = ""
        outfile.write("\n"+line[:-1])
    else:                                                              
        comp += line
'''


#Exercise 2
'''
def factorial(number):                                                  #Function for calculating the factorial
    factorial = 1
    for i in range(2, number+1):
        factorial *= i
    return factorial

number = int(input("Please enter a positive integer: "))
if number >= 0:                                                         #Input control, needs to be a positive integer
    print("Factorial of" , number , "is" , factorial(number))
else:
    print("You did not enter a non-negative integer.")
'''

#Exercise 3
'''
user = input("Enter three letter aminoacid sequence: ")

def codon(aa):                                                                          #Function for translation of a three letter aminoacid sequence
    lu_table = dict()
    lu_table = dict.fromkeys(['ATT', 'ATC', 'ATA'], 'I')
    lu_table.update(dict.fromkeys(['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'], 'L'))
    lu_table.update(dict.fromkeys(['GTT', 'GTC', 'GTA', 'GTG'], 'V'))
    lu_table.update(dict.fromkeys(['TTT', 'TTC'], 'F'))
    lu_table.update(dict.fromkeys(['ATG'], 'M'))
    lu_table.update(dict.fromkeys(['TGT','TGC'], 'C'))
    lu_table.update(dict.fromkeys(['GCT', 'GCC', 'GCA', 'GCG'], 'A'))
    lu_table.update(dict.fromkeys(['GGT', 'GGC', 'GGA', 'GGG'], 'G'))
    lu_table.update(dict.fromkeys(['CCT', 'CCC', 'CCA', 'CCG'], 'P'))
    lu_table.update(dict.fromkeys(['ACT', 'ACC', 'ACA', 'ACG'], 'T'))
    lu_table.update(dict.fromkeys(['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'S'))
    lu_table.update(dict.fromkeys(['TAT', 'TAC'], 'Y'))
    lu_table.update(dict.fromkeys(['TGG'], 'W'))
    lu_table.update(dict.fromkeys(['CAA', 'CAG'], 'Q'))
    lu_table.update(dict.fromkeys(['AAT', 'AAC'], 'N'))
    lu_table.update(dict.fromkeys(['CAT', 'CAC'], 'H'))
    lu_table.update(dict.fromkeys(['GAA', 'GAG'], 'E'))
    lu_table.update(dict.fromkeys(['GAT', 'GAC'], 'D'))
    lu_table.update(dict.fromkeys(['AAA', 'AAG'], 'K'))
    lu_table.update(dict.fromkeys(['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'R'))
    lu_table.update(dict.fromkeys(['TAA', 'TAG', 'TGA'], 'Stop codon'))
    
    if aa in lu_table:                                                                  #Input control, if the user input is not an codon, gives an error.
        codon = lu_table[aa]
    else:
        codon = "This is not a proper aminoacid sequnce"
    return codon

print(codon(user))
'''

#Exercise 4
'''
import math

infile = open('ex1.dat', 'r')
numbers = list()
total_num = 0
mean = 0
x = 0
for line in infile:                                    #Splits numbers and add them to a list
    numbers += line.split()

for num in numbers:                                     #Converts strings to float and sums them
    mean += float(num)
    total_num += 1

mean = mean/total_num                                   #Calculates the mean value

for i in numbers:                                       #Calculates the upper part of the equation. (x-mean)**2
    x += (float(i) - mean)**2

result = math.sqrt(x/total_num)                         #Results
    
print(result)


'''
#Exercise 5
'''
import sys
try:
    accFile = open("ex5.acc", 'r')
except IOError as e:
    print("Can't open file, Reason: " + str(e))
    sys.exit(1)

accessions = dict()
for acc in accFile:                                     #Loop that counts the number of accessions
    acc = acc.strip()
    if acc in accessions:
        accessions[acc] += 1
    else:
        accessions[acc] = 1
accFile.close()

sorted_dict = reversed(sorted(accessions.values()))     #Sort the accession values and reverses it.
result = dict()
for i in sorted_dict: 
    for x in accessions.keys():
        if accessions[x] == i:
            result[x] = accessions[x]
print(result)
'''
