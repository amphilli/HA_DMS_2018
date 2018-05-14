1. In the main directory (XBP139vsDMSO39/)

Input:

Rep1_XBP139_mutdiffsel.txt
Rep2_XBP139_mutdiffsel.txt
Rep3_XBP139_mutdiffsel.txt

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


2. In the compare directory (XBP139vsDMSO39/compare)

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

