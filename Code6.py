#!/usr/bin/env python3

#Exerise 1

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
lu_table.update(dict.fromkeys(['TAA', 'TAG', 'TGA'], 'Stop'))


#Exercise 2

import re

infile = open('dna7.fsa', 'r')
outfile = open('aa7.fsa', 'w')
aa_seq = ""

for line in infile:                                                     #For loop finds the line that starts with '>', and while the string is empty, outwrite the variable complement.
    if line.startswith('>'):
        outfile.write(line[:-1] + ' AA sequence')
    else:
        for i in range(0,len(line),3):                                  #Same as before, but starts at a new reading frame
            codon = line[i:i+3]
            if codon in lu_table:
                aa_seq += lu_table[codon]
    outfile.write(aa_seq + "\n")
    aa_seq = ""

#Exercise 3

infile = open("start10.dat", "r")
infile2 = open("res10.dat", "r")

start = set()
res = set()
miss = set()

#Adding each acc numb to a set() variable
for line in infile:
    start.add(line[:-1])

#Adding each acc numb to a set() variable
for line2 in infile2:
    acc = line2.split()
    res.add(acc[1])

#Iterating the start set(), and if the acc numb is not in the res set(), add the acc numb to a new set() variable.
for i in start:
    if i not in res:
        miss.add(i)

print(miss)


#Exercise 4

infile = open("ex5.acc", "r")
lists = []
counts = dict()

for i in infile:                                                            #Iterating lines in file and saving them to a list
    lists.append(i[:-1])
infile.close()

for i in lists:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

outfile = open("ex5ress.acc", "w")
for i in sorted(counts.keys()):
    outfile.write('{}: {:1d}\n'.format(i, counts[i]))


#Exercise 5

import re

infile = open("data1.gb", "r")
flag = False
joinflag = False
joinline = ""
dna = ""
for line in infile:
    if line[:-1] == "//":                                                       #If line starts with "//" at position[:-1], set flag as False
        flag = False
    if flag:                                                                    #While the flag is true, add the line to dna.
        dna += line[10:-1]
        dna = dna.replace(' ', '')
    if line[:6] == "ORIGIN":                                                    #If "ORIGIN" is present at position[:6], set flag as True
        flag = True   
    # Find exons - the join line(s)
    REresult = re.search(r'^\s+CDS\s+join\((.+)', line)
    if REresult is not None:
        joinline += REresult.group(1).strip()
        if line[-2] != ')':				
            joinflag = True
    elif joinflag:
        joinline += line.strip()
        if line[-2] == ')':				
            joinflag = False
            
exons = joinline[:-1].split(',')
cds = ''

for exon in exons:                                                              #As the exons on the line is ".." seperated, we split it
    pos = exon.split(r'..')
    start = int(pos[0]) - 1                                                     #Defines start and end of the coding dna
    end = int(pos[1])
    cds += dna[start:end]                                                       #Adding the dna[start:end] to the cds variable.
    cds = cds.upper()
print("Coding DNA sequence:")
for i in range(0, len(cds), 60):
    print(cds[i:i+60])    

codon = []
codon_list = []
counts = dict()
for i in range(0, len(cds), 3):                                                 #Splits the dna into codons and saves them in the codon variable
    codon.append(cds[i:i+3])

for i in codon:                                                                 #If codon in look up table, count[i] +1 else set it as 1. 
    if i in lu_table.keys():
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            
print(counts)


#Exercise 6

import re

infile = open("data2.gb", "r")                                              

res = ""
names = []
author = []

for line in infile:                                                         #Iterating file
    if line.startswith('  AUTHORS'):                                        #Finding lines that starts with author
        res = re.search(r'^\s+\w+\s+(.+)', line).group(1)                   #Grabs all names on the line
        res = res.replace("and", ",")                                       #Replace "and" with ",", which makes the line comma/space seperated by the name.
        res =res.split(", ")                                                #Split line by comma/space
        for i in res:                                                       #Iterating the split line and appends the name to a variable. 
            names.append(i)
        
for i in names:                                                             #Iterating saved names, and if the name is not in the authors list, append it to the list.
    if i not in author:
        author.append(i)

print(author)