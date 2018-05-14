This module filters mutdiffsel data from dms_tools:
(1) removes all mutdiffsel values for variants not present in the starting library of the corresponding replicate, replacing that mutdiffsel value with -100 in an array which is then plotted on a heatmap (where -100 is colored in black).
(2) removes mutdiffsel values that are not of the same sign (positive or negative) across replicates. values that are removed are replaced with -100 in the "pickouts" files and are shaded white in the heatmaps.

Details about input/output/code are in each selection sub-directory