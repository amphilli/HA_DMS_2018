#!/bin/env python
import numpy as np
import sys

aa={0:'G',1:'A',2:'V',3:'I',4:'L',5:'M',6:'F',7:'Y',8:'W',9:'S',10:'T',11:'N',12:'Q',13:'C',14:'P',15:'H',16:'R',17:'K',18:'D',19:'E'}

dataFile1 = sys.argv[1]
dataFile2 = sys.argv[2]
dataFile3 = sys.argv[3]

nres=565
nmut=20

data1 = np.zeros((nres,nmut))
data2 = np.zeros((nres,nmut))
data3 = np.zeros((nres,nmut))

data12 = np.zeros((nres,nmut)) # here data is the overlap b/t data1 and data2, normalized by 0.5(sum_data1^2+sum_data2^2)
data13 = np.zeros((nres,nmut)) # here data is the overlap b/t data1 and data2, normalized by 0.5(sum_data1^2+sum_data2^2)
data23 = np.zeros((nres,nmut)) # here data is the overlap b/t data1 and data2, normalized by 0.5(sum_data1^2+sum_data2^2)

with open(dataFile1) as f1:
  ires=0
  for line in f1:
    parts = line.split()
    #print parts
    for i in range(nmut):
      data1[ires,i]=float(parts[i])
    ires+=1

with open(dataFile2) as f2:
  ires=0
  for line in f2:
    parts = line.split()
    #print parts
    for i in range(nmut):
      data2[ires,i]=float(parts[i])
    ires+=1

with open(dataFile3) as f3:
  ires=0
  for line in f3:
    parts = line.split()
    #print parts
    for i in range(nmut):
      data3[ires,i]=float(parts[i])
    ires+=1

picks = np.zeros((nres,nmut)) 
nrep=3
sampled_rep = np.zeros((nrep,nres)) 
sampled_sum = np.zeros(nrep)
sampled_avg = np.zeros(nrep)
sampled_in_all_reps = np.zeros(nres)
ncount = 0 # number of mutations that consistently > 0 or < 0 in all 3 replicates
avgmax=0
avgmin=0
with open('out_list_pickouts_pos.txt','w') as flistp:
 with open('out_list_pickouts_neg.txt','w') as flistn:
  for n in range(nres):
   print 'res',n
   for i in range(nmut):
     v1 = data1[n,i]
     v2 = data2[n,i]
     v3 = data3[n,i]
     print n, aa[i],v1,v2,v3
     if v1 > -100:
         sampled_rep[0,n] += 1
     if v2 > -100:
         sampled_rep[1,n] += 1
     if v3 > -100:
         sampled_rep[2,n] += 1
     if v1 == -100 and v2 == -100 and v3 == -100:
       avg = -100 # all three replicas did not have this mutation in the starting library
     elif v1 > -100 and v2 > -100 and v3 > -100:
       sampled_in_all_reps[n] += 1
       if v1 > 0 and v2 > 0 and v3 > 0:
         avg = (v1+v2+v3)/3.0 
         ncount += 1
         flistp.write('%3d %s %8.5f %8.5f %8.5f %8.5f \n' % (n, aa[i], avg, data1[n,i], data2[n,i], data3[n,i]))
       elif v1 < 0 and v2 < 0 and v3 < 0:
         avg = (v1+v2+v3)/3.0 
         ncount += 1
         flistn.write('%3d %s %8.5f %8.5f %8.5f %8.5f \n' % (n, aa[i], avg, data1[n,i], data2[n,i], data3[n,i]))
       else: 
         avg = -100 # ambiguous
     else:
         avg = -100 
     picks[n,i]=avg
     if avg > avgmax and avg < 100 : 
       avgmax=avg
       nmax = n
       imax = i
     if avg < avgmin and avg > -100: 
       avgmin=avg
       nmin = n
       imin = i
   
print "Number of mutations that consistently have > 0 or < 0 in all three replicates = ",ncount
print "Most positive avg selection: ",avgmax, "at res ",nmax, " (+1) with mutation ",aa[imax],data1[nmax,imax],data2[nmax,imax],data3[nmax,imax]
print "Most negative avg selection: ",avgmin, "at res ",nmin, " (+1) with mutation ",aa[imin],data1[nmin,imin],data2[nmin,imin],data3[nmin,imin]

print "Remember to change the range in the gnuplot accordingly"
 
norm1=0.0
norm2=0.0
norm3=0.0
for n in range(nres):
  for i in range(nmut):
    v1 = data1[n,i]
    v2 = data2[n,i]
    v3 = data3[n,i]
    if v1 > -100.0 and v2 > -100.0:
      data12[n,i]=v1*v2
    if v1 > -100.0 and v3 > -100.0:
      data13[n,i]=v1*v3
    if v2 > -100.0 and v3 > -100.0:
      data23[n,i]=v2*v3
    if v1 > -100.0:
      norm1+=v1*v1
    if v2 > -100.0:
      norm2+=v2*v2
    if v3 > -100.0:
      norm3+=v3*v3

NIP12=0.0
norm=0.5*(norm1+norm2)
for n in range(nres):
  for i in range(nmut):
    data12[n,i]=data12[n,i]/norm
    NIP12+=data12[n,i]

NIP13=0.0
norm=0.5*(norm1+norm3)
for n in range(nres):
  for i in range(nmut):
    data13[n,i]=data13[n,i]/norm
    NIP13+=data13[n,i]

NIP23=0.0
norm=0.5*(norm2+norm3)
for n in range(nres):
  for i in range(nmut):
    data23[n,i]=data23[n,i]/norm
    NIP23+=data23[n,i]

print 'NIP12 = ',NIP12
print 'NIP13 = ',NIP13
print 'NIP23 = ',NIP23

#with open('out_v1v2.txt', 'w') as fout:
#  for n in range(nres):
#    fout.write('%8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f \n' % (data[n,0],data[n,1],data[n,2],data[n,3],data[n,4],data[n,5],data[n,6],data[n,7],data[n,8],data[n,9],data[n,10],data[n,11],data[n,12],data[n,13],data[n,14],data[n,15],data[n,16],data[n,17],data[n,18],data[n,19]))

sampled_in_all_sum = 0
for n in range(nres):
  sampled_in_all_sum += sampled_in_all_reps[n] 
  for m in range(nrep):
    sampled_sum[m] = sampled_sum[m]+sampled_rep[m,n]

with open('out_sampled_rep_all3_WTincluded.txt', 'w') as foutS:
  for n in range(nres):
    foutS.write('%d %d %d %d \n' % \
    #foutS.write('%8.5f %8.5f %8.5f \n' % \
(sampled_rep[0,n], sampled_rep[1,n], sampled_rep[2,n], sampled_in_all_reps[n]))
  foutS.write('%d %d %d %d \n' % (sampled_sum[0], sampled_sum[1], sampled_sum[2], sampled_in_all_sum))

with open('out_heatmaps_all3.txt', 'w') as foutA:
  for n in range(nres):
    foutA.write('%8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f \
%8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f \
%8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f \n' % \
(data1[n,0],data2[n,0],data3[n,0],\
data1[n,1],data2[n,1],data3[n,1],\
data1[n,2],data2[n,2],data3[n,2],\
data1[n,3],data2[n,3],data3[n,3],\
data1[n,4],data2[n,4],data3[n,4],\
data1[n,5],data2[n,5],data3[n,5],\
data1[n,6],data2[n,6],data3[n,6],\
data1[n,7],data2[n,7],data3[n,7],\
data1[n,8],data2[n,8],data3[n,8],\
data1[n,9],data2[n,9],data3[n,9],\
data1[n,10],data2[n,10],data3[n,10],\
data1[n,11],data2[n,11],data3[n,11],\
data1[n,12],data2[n,12],data3[n,12],\
data1[n,13],data2[n,13],data3[n,13],\
data1[n,14],data2[n,14],data3[n,14],\
data1[n,15],data2[n,15],data3[n,15],\
data1[n,16],data2[n,16],data3[n,16],\
data1[n,17],data2[n,17],data3[n,17],\
data1[n,18],data2[n,18],data3[n,18],\
data1[n,19],data2[n,19],data3[n,19]))

with open('out_heatmaps_pickouts.txt','w') as foutPO:
  for n in range(nres):
    foutPO.write('%8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f \n' % \
(picks[n,0], picks[n,1], picks[n,2], picks[n,3], picks[n,4],picks[n,5],picks[n,6],picks[n,7],picks[n,8],picks[n,9],\
picks[n,10], picks[n,11], picks[n,12], picks[n,13], picks[n,14],picks[n,15],picks[n,16],picks[n,17],picks[n,18],picks[n,19]))

with open('out_scatter_12.txt', 'w') as fout2:
  for n in range(nres):
    for i in range(nmut):
      fout2.write('%8.5f %8.5f %s %d \n' % (data1[n,i],data2[n,i],aa[i],i))

with open('out_scatter_13.txt', 'w') as fout2:
  for n in range(nres):
    for i in range(nmut):
      fout2.write('%8.5f %8.5f %s %d \n' % (data1[n,i],data3[n,i],aa[i],i))

with open('out_scatter_23.txt', 'w') as fout2:
  for n in range(nres):
    for i in range(nmut):
      fout2.write('%8.5f %8.5f %s %d \n' % (data2[n,i],data3[n,i],aa[i],i))

for i in range(nmut):
  with open('out_scatter_12_%s.txt' % aa[i], 'w') as fout:
    for n in range(nres):
      fout.write('%8.5f %8.5f \n' % (data1[n,i],data2[n,i]))

for i in range(nmut):
  with open('out_scatter_13_%s.txt' % aa[i], 'w') as fout:
    for n in range(nres):
      fout.write('%8.5f %8.5f \n' % (data1[n,i],data3[n,i]))

for i in range(nmut):
  with open('out_scatter_23_%s.txt' % aa[i], 'w') as fout:
    for n in range(nres):
      fout.write('%8.5f %8.5f \n' % (data2[n,i],data3[n,i]))


