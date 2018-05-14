#!/bin/env python
import numpy as np
import sys

aa={0:'G',1:'A',2:'V',3:'I',4:'L',5:'M',6:'F',7:'Y',8:'W',9:'S',10:'T',11:'N',12:'Q',13:'C',14:'P',15:'H',16:'R',17:'K',18:'D',19:'E'}

dataFile1 = sys.argv[1] # read in a sorted list
dataFile2 = sys.argv[2] # read in WT sequence
dataFileO = sys.argv[3] # name of the output file for making logo plot 

nres=565
nmut=20

avgsel=np.zeros((nres,nmut)) # avg selection at each site for each mutation
WT=np.chararray((nres)) # WT seq

with open(dataFile1) as f1:
  for line in f1:
    parts = line.split()
    ires=int(parts[0]) # site 
    mut=parts[1] # mustation
    avg=float(parts[2]) # avg sel
    for k in aa.keys():
      if aa[k] == mut:
         imut=k
    avgsel[ires,imut]=avg

with open(dataFile2) as f2:
  for line in f2:
    parts = line.split()
    ires=int(parts[0])-1 # site (make indexing start at 0) 
    res=parts[2] # WT seq
    #print res
    WT[ires]=res

with open(dataFileO,'w') as fout:
  for i in range(nres):
    for k in range(nmut):
      fout.write('%d,%s,%s,%8.5f \n' % ((i+1),WT[i],aa[k],avgsel[i,k]))


