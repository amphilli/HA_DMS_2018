This folder contains all code and results for analysis downstream of calculating the differential selection via dms_tools.

The python scripts in this folder were written by Prof. Yu-Shan Lin of Tufts University to assist in filtering and visualization of deep mutational scanning data.

In this directory are three sub-directories containing data anlaysis modules:
1. filtering: filters replicate mutdiffsel data from dms_tools and creates text files and heatmaps of filtered data
2. sitediffsel: calculates the site differential selection from filtered output
3. for_logo_plot: takes filtered output and formats it to be used as input for dms_logoplot

Each sub-directory contains a readme file describing the contents as well as one sub-directory for each differential selection comparison:
	DMSO39vsDMSO37
	DAX39vsDAX37
	XBP139vsXBP137
	XBP137vsDMSO37
	XBP139vsDMSO39
	DAX37vsDMSO37
	DAX39vsDMSO39

