
#input files need to be in the fasta format containing raw reads 

#ignore first line => info about organism 
#read in the base pairs 
def readGenome(filename):
  genome = ' '
  with open(filename , 'r') as f:
    for line in f:
      if not line[0] == '>':
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
  

