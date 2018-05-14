This module takes output from the filtering module and creates a site differential selection file by summing the mutation differential selection values at each site.

Input files:
  (1) out_heatmap_pickouts.txt #output from filtering module
    each of these should have 565 lines
    each line has 20 numbers, which are the selections of the 20 aa for that residue
    if that aa did not exist for that residue in the starting library, i put -100 as its selection so i can tell it from the others
  (2) Py_calc_site_diffsel.py
 
To run:
  python Py_calc_site_diffsel.py out_heatmap_pickouts.txt

Output files:
  out_diffsel_pickouts_samplename.txt
    column 1: pos sel
    column 2: neg sel
    column 3: pos sel + neg sel
    column 4: pos sel - neg sel = |pos sel| + |neg sel|
