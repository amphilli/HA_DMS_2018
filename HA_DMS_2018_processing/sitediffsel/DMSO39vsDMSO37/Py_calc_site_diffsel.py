#!/bin/env python
import numpy as np
import sys

aa={0:'G',1:'A',2:'V',3:'I',4:'L',5:'M',6:'F',7:'Y',8:'W',9:'S',10:'T',11:'N',12:'Q',13:'C',14:'P',15:'H',16:'R',17:'K',18:'D',19:'E'}

dataFile1 = sys.argv[1]

nset=1
nres=565
nmut=20

data = np.zeros((nset,nres,nmut))
possel = np.zeros((nset+1,nres))
negsel = np.zeros((nset+1,nres))

with open(dataFile1) as f1:
  iset=0
  ires=0
  for line in f1:
    parts = line.split()
    #print parts
    for i in range(nmut):
      val = float(parts[i])
      data[iset,ires,i]=val
      if val > -100.0 and val > 0:
        possel[iset,ires]+=val
      if val > -100.0 and val < 0:
        negsel[iset,ires]+=val
    ires+=1

for m in range(nset):
  with open('out_diffsel_pickouts_DMSOtemp.txt', 'w') as fout:
    for n in range(nres):
      possel[nset,n]+=possel[m,n]
      negsel[nset,n]+=negsel[m,n]
      fout.write('%d %8.5f %8.5f %8.5f %8.5f \n' % (n+1, possel[m,n], negsel[m,n], possel[m,n]+negsel[m,n], possel[m,n]-negsel[m,n]) )


