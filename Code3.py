#!/bin/python3

## Exercise 1,2,3
'''
#file = input("Enter a file name:\n")
infile = open("sprot1.dat", "r")

for line in infile: 
    if "AC   " in line:
        accession = line.split()
        print(accession[1])
    elif "ID   " in line: 
        ID = line.split()
        print(ID[1])
infile.close
        
'''

#Exercise 4
'''
infile = open("sprot1.dat", "r")

(data, seqflag) = ('', False)
for line in infile:
    if line[:-1] == "//":
        seqflag = False
    if seqflag:
        data += line[5:-1]
    if line[:2] == "SQ":
        seqflag = True

if seqflag:
    raise ValueError("Format is not right. Can’t trust result")

print(data)
infile.close

'''

#Exercise 5
'''

infile = open("sprot1.dat", "r")

(data, seqflag) = ('', False)
for line in infile:
    if line[:2] == "SQ" in line: 
        aa = line.split()
        aa_num = int(aa[2])
    if line[:-1] == "//":
        seqflag = False
    if seqflag:
        data += line[5:-1]
    if line[:2] == "SQ":
        seqflag = True

if seqflag:
    raise ValueError("Format is not right. Can’t trust result")

data = data.replace(" ", "")
aa_len = len(data)

if aa_len == aa_num:
    print("The sequence length is correct!\n", "File aa num: ", aa_num, "\n", "Length of extracted sequence: ", aa_len)
else: 
    print("!FALSE! The sequence is not the same length!\n", "File aa num: ", aa_num, "\n", "Length of extracted sequence: ", aa_len)
    
infile.close

'''
#Exercise 6
'''
infile = open("sprot1.dat", "r")
outfile = open("sprot1.fsa", "w")

(data, seqflag) = ('', False)
for line in infile:                                                         #Iterates each line in the file.
    if "AC   " in line:                                                     #If "AC    " is present, split the line and saves the accession num
        accession = line.split()
        print(accession[1])
    if "ID   " in line:                                                     #Same as before but with the ID
        ID = line.split()
        print(ID[1])
    if line[:2] == "SQ" in line:                                            #Same as before but with the sequence length
        aa = line.split()
        aa_num = aa[2]
    if line[:-1] == "//":                                                   #Stateful parsing, when "SQ" is present, start adding the lines into the data variable
        seqflag = False
    if seqflag:
        data += line[5:-1]
    if line[:2] == "SQ":
        seqflag = True

if seqflag:
    raise ValueError("Format is not right. Can’t trust result")

data = data.replace(" ", "")                                                #Removes spaces in the sequence
aa_len = len(data)                                                          #Calculates the len of the data string

outfile.write(">"+accession[1]+ID[1]+"\t"+aa_num+"AA"+"\n")                  
for i in range(0,len(data),60):                                             #For loop, that iterates 60AA at a time and write it into the output file. 
    data_new = data[i:i+60]
    print(data_new)
    outfile.write(data_new + "\n")
    
infile.close
outfile.close
'''


#Exercise 7
'''
infile = open("dna.fsa", "r")                                   #Read file and skip first line
next(infile)
data = ""
for line in infile:                                             #Iterates lines and saves DNA into data string
    data += line[:-1]

codon = []
for i in range(0,len(data),3):                                  #For loop that slits up the sequence into 3AA
    start = data[i:i+3]
    if start=='ATG':                                            #If "ATG" is present in the iteration, append the position of the codon to the codon list
        codon.append(i+1)

for i in range(1,len(data),3):                                  #Same as before, but starts at a new reading frame
    start = data[i:i+3]
    if start=='ATG':
        codon.append(i+1)        

for i in range(2,len(data),3):
    start = data[i:i+3]
    if start=='ATG':
        codon.append(i+1)

codon.sort()
print(codon)
'''

#Exercise 8 
'''
Open file
Skip first line
creating empty variable

iterating each line in file
    add each line to empty variable without newline

creating empty list

iterating each char in range of first start codon to the total len of data with 3 steps 
    Saves each iterating into new variable (start)
    if start contains "TTA"
        append the iteration number to the empty list
    if start contains "TAG"
        append the iteration number to the empty list
    if start contains "TGA"
        append the iteration number to the empty list
print list of stop codons in the sequence. 
'''

'''
infile = open("dna.fsa", "r")
next(infile) 
data = ""
for line in infile:
    data += line[:-1]

stop_codon = []

for i in range(data.find("ATG"),len(data),3):
    start = data[i:i+3]
    if start=='TAA':
        stop_codon.append(i+1)
    if start=='TAG':
        stop_codon.append(i+1)
    if start=='TGA':
        stop_codon.append(i+1)
print(stop_codon)
'''
#Exercise 9
'''
infile = open("orphans.sp", "r")
organism = input("Enter the name of the organism:\n")               #Asks for input
result = 0

for line in infile:                                                 #Iterates each line in the file,
    if organism.upper() in line:                                    #If the user input word is present in the line, add +1 to the result variable
        result += 1

if result != 0:                                                     #Printing the total amount of lines with the user input in it. 
    print("Total lines with", organism, "in it: ", result)
else: 
    print("Something went wrong, not a valid organism")             #If there is none in the lines, display an error message. 
'''

#Exercise 10 Brain stopped working, error 404.


