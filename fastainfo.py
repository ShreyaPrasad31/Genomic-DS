 
#input files need to be in the fasta format containing raw reads 

#ignore first line => info about organism 
#read in the base pairs 
def readGenome(filename):
  genome = ' '
  with open(filename , 'r') as f:
    for line in f:
      if not line[0] == '>': #ignore the first line of the fasta file, which contains information about the machine 
        genome+ = line.rstrip()
    return genome 
  
genome = readGenome('lambds_virus.fa')  

#count the frequency of each base
counts = {'A' : 0 , 'C' : 0 , 'G' :0 , 'T' : 0}
for base in genome:
  counts[base]+ = 1
print(counts)

##################################or#####################
import collections 
collections.counter(genome)
  
#phred--33
#quality values for the reads 
#each quality score is phred 33 encoded
def QtoPhred33(Q): #conver to ASCII vaue 
  return chr(Q + 33) #Q must be rounded up to the nearest integer
def Phred33toQ(qval)
return ord(qval) - 33
#download human sequencing reads 
#!wget --no-check url(conf)

#parse the dataset, two seperate lists, one for next generation seq, other for the qaulity scores of the bases 
#the quality score(Phred 33 encoded ) of the nucleotide lies directly below the sequence of raw reads 
def ReadFastQ(filename):
  sequences = []
  qualities = []
  with open (filename) as fh:
    while True:
      fh.readline()
      seq = fh.readline().rstrip()
      fh.readline
      qual = fh.readline().rstrip()
      if len(seq) == 0 :
        break
      sequences.append(seq)
      qualities.append(qual)
 return qualities, sequences   

#analyze the parsed data
def createHist(qualities):
  hist = [0]*50
  for qual in qualities:
    for phred in qual:
      q = Phred33toQ(phred)
      hist[q]+ = 1
  return hist    

import matplotlib.pyplot as plt
plt.bar(range(len(h)) , h)
plt.show()

#find the GC content
def findGCbypos(reads):
  gc = [0]*100
  totals = [0]*100
  for read in reads:
    for i in range(len(reads)):
      if read[i] == 'C' or read[i] =='G':
        gc[i]+ = 1
        totals[i]+ = 1
    for i in range(len(gc)):
      if totals[i] > 0:
        gc[i]/ = float(totals[i])
gc = findGCbypos(range(len(gc)) , gc)
plot.show()
#average GC content of the human genome is greater than 1/2 usually

#counts of different bases in the sequence
import collections
count = collections.Counter()
for seq in seqs:
  count.update(seq)
print(count) #=> will have a value of N when the base caller sequencer has no confidence   
        
#reference based assembly of base snippets to an already known genome 
#how many times the pattern P occurs in the text T


#Naive Algorithm
def naive(p,t):
  occurences = []
  for i in range(len(t) - len(p) + 1):
    match = True
    for j in range(len(p)):
      if t[i+i]! = p[j]:
        match = False # =/REJECT ALIGNMENT 
        break
      if match:
        occurences.append(i)
 return occurences 

#x = |p| , y = |t| , worst case alignment will iterate x(y-x+1) times
#best case y-x+1 , one character comparison per alignment

#Matching artificial reads
!wget --no-check http://d28rg4awqoiu5.cloudfront.net/ads1/data/phix.fa
genome = readGenome('phix.fa.1')

  

  

