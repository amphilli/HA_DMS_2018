This folder contains one subdirectory for each differential selection comparison. This module formats the pickouts output from the filtering modules into a form that can be used as input for dms_logoplot to generate sequence logo plots. To do this, it adds the WT WSN HA sequence, changes the indexing to start at 1 to match the site numbers in the reference sequence, and reformats the data for dms_logoplot.

Before running: combine the the out_list_pickouts_neg.txt and out_list_pickouts_pos.txt into one file (_all_pickouts.txt) and then sort by site (col[0]) in ascending order(_all_pickouts_sorted.txt).


Input:
HAalignment_v2.txt #contains wt sequence
*_all_pickouts_sorted.txt #sorted output of filtering module


Output:
*_all_pickouts_sorted_for_logo_HA.txt #can be used as input for dms_logoplot


Code:

Py_add_WT_info_logo_plot.py


To run:

python2.7 Py_add_WT_info_logo_plot.py *_all_pickouts_sorted.txt HAalignment_v2.txt *_all_pickouts_sorted_for_logo_HA.txt
