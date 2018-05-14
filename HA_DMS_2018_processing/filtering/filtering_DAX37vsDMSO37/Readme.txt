1. In the main directory (DAX37vsDMSO37/)

#this script removes all mutdiffsel values for variants not present in the starting library of the corresponding replicate, replacing that mutdiffsel value with -100 in an array which is then plotted on a heatmap (where -100 is colored in black).

Input:

#Output files from dms_diffselection:
Rep1_DAX37_mutdiffsel.txt
Rep2_DAX37_mutdiffsel.txt
Rep3_DAX37_mutdiffsel.txt

#Output files from dms_barcodedsubamplicions (first replace codon labels with amino acid labels)
LIB1_countsAAcodons.txt
LIB2_countsAAcodons.txt
LIB3_countsAAcodons.txt

Codes:

labels_aa.txt
Py_heatmap_template_v2.py
Gnuplot_heatmap.gplt

Sh_1_genHeatMaps.sh # need to change the name field in this file to match the title in the mutdiffsel.txt files

To run:

./Sh_1_genHeatMaps.sh


2. In the compare directory (DAX3739vsDMSO37/compare)

#this script uses the output from the above script to remove mutdiffsel values that are not of the same sign (positive or negative) across replicates. values that are removed are replaced with -100 in the "pickouts" files and are shaded white in the heatmaps.

Input: 

out_heatmap_rep1.txt # copy from the results in rep1/ rep2/ rep3/ directory from step 1
out_heatmap_rep2.txt
out_heatmap_rep3.txt

Codes:

labels_aa.txt
Py_compare_heatmaps.py
Gnuplot_3heatmaps.gplt

To run:

./Sh_2_compareHeatMaps.sh # should change the name and title fields in this file to match the description

