
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
  
