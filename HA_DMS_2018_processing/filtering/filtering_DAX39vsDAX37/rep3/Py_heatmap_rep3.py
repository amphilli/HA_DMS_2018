#!/bin/env python
import numpy as np
import sys

dataFile = sys.argv[1]
nomutFile = sys.argv[2]

nres=565
nmut=20

data = np.zeros((nres,nmut))

aa={0:'G',1:'A',2:'V',3:'I',4:'L',5:'M',6:'F',7:'Y',8:'W',9:'S',10:'T',11:'N',12:'Q',13:'C',14:'P',15:'H',16:'R',17:'K',18:'D',19:'E'}

with open(dataFile) as f:
  for line in f:
    line_no_nw = line.rstrip('\n')
    parts = line_no_nw.split(',')
    ires = int(parts[0])-1 # note: ires starts at 0
    mut = parts[2]
    for k in aa.keys():
       if aa[k] == mut:
          imut=k
    sel = parts[3]
    data[ires,imut]=sel

# For mutations that did not exist in the library, make their selection values -100

col = np.zeros((100,), dtype=np.int)
for i in range (len(col)):
  col[i] = 99

count_mut = np.zeros((nres,nmut))
with open(nomutFile) as f2:  
  for i, line in enumerate(f2):
    if i == 0: # header
      line_no_nw = line.rstrip('\n')
      parts = line_no_nw.split('\t')
      ncol = len(parts)
      #print 'ncol = ',ncol
      for j in range(2,ncol):
        mut = parts[j]
        print mut
        for k in aa.keys():
          if aa[k] == mut:
            col[j]=k 
        #print mut, k, aa[col[j]]
    else:
      line_no_nw = line.rstrip('\n')
      parts = line_no_nw.split()
      ncol = len(parts)
      ires = int(parts[0])-1 # note: ires starts at 0
      for j in range(2,ncol):
         imut=col[j]
         print ires, j,imut # New
         if imut < 20:  # New
           count_mut[ires,imut]+=int(parts[j]) # New
         #print ires,aa[imut],count_mut[ires,imut]

for n in range(nres):
  for i in range(nmut):
    if count_mut[n,i] == 0:
       #print 'res', n, 'mutation', aa[i], 'has zero counts'
       data[n,i]=-100.0

with open('out_heatmap_rep3.txt', 'w') as fout:
  for n in range(nres):
    fout.write('%8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f \n' % (data[n,0],data[n,1],data[n,2],data[n,3],data[n,4],data[n,5],data[n,6],data[n,7],data[n,8],data[n,9],data[n,10],data[n,11],data[n,12],data[n,13],data[n,14],data[n,15],data[n,16],data[n,17],data[n,18],data[n,19]))

