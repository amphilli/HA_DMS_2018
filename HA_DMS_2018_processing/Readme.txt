This directory contains all code and results for analysis downstream of calculating the differential selection via dms_tools[ref].

The python scripts in this folder were written by Prof. Yu-Shan Lin of Tufts University to assist in filtering and visualization of deep mutational scanning data.

In this directory are four sub-directories containing data anlaysis modules:
1. filtering: filters replicate mutdiffsel data from dms_tools and creates text files and heatmaps of filtered data
2. sitediffsel: calculates the site differential selection from filtered output
3. for_logo_plot: takes filtered output and formats it to be used as input for dms_logoplot
4. logo_plots: this folder contains the input and output for running dms_logoplot, which is part of the dms_tools package.
5. structure: maps sitediffsel values onto HA structure (PDB ID 1RVX)--this analysis was performed for DMSO39vsDMSO37 and XBP139vsDMSO39.

Sub-directories 1–3 contain a readme file describing the contents as well as one sub-directory for each differential selection comparison:
	DMSO39vsDMSO37
	XBP137vsDMSO37
	XBP139vsDMSO39
	DAX37vsDMSO37
	DAX39vsDMSO39
	DAX39vsDAX37*
	XBP139vsXBP137*

*Note that these comparisions are not discussed explicitly in the manuscript. The analysis is provided for sake of completeness.
