This module takes output from the filtering module (for each replicate library) and creates a site differential selection file by summing the mutation differential selection values at each site.

Input files:
  (1) out_heatmap_rep1.txt out_heatmap_rep2.txt out_heatmap_rep3.txt
    each of these should have 565 lines
    each line has 20 numbers, which are the mut diffsel values of the 20 aa for that residue
    if that aa did not exist for that residue in the starting library, -100 is noted as its diffsel to distinguish it from true diffsel values
  (2) Py_calc_site_diffsel.py
 
To run:
  python Py_calc_site_diffsel.py out_heatmap_rep1.txt out_heatmap_rep2.txt out_heatmap_rep3.txt

Output files:
  out_diffsel_rep1.txt out_diffsel_rep2.txt out_diffsel_rep3.txt and out_diffsel_avg.txt
    column 1: pos sel
    column 2: neg sel
    column 3: pos sel + neg sel
    column 4: pos sel - neg sel = |pos sel| + |neg sel|