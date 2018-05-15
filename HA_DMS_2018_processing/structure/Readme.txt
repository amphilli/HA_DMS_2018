This module maps the sitediffsel values from module 2 onto the HA structure:

With 1RVX_trimer_correctnumbering open in PyMol:

Navigate to directory with site differential selection values:
This should be a text file of net site differential selection values (col[4] of sitediffsel module), excluding values for sites that are missing in structure (1–17, 341–343, 504–565). It should be copied three times in the file so that site differential selection values are mapped to all three monomers in the structure.

Once in directory, run the following commands in PyMol:

#store site differential selection values as B-factors
inFile = open(“file_name.txt”, ‘r’)
stored.newB=[]
for line in inFile.readlines(): stored.newB.append( float(line) )
inFile.close()

#zero B-factors
alter 1RVX_trimer_correctnumbering, b=0.0

#replace B-factors with differential selection values for residue alpha-carbons
alter 1RVX_trimer_correctnumbering and n. CA, b=stored.newB.pop(0)

#color based on B-factors, setting color scale, thresholds, and coloring entire residue
spectrum b, blue_gray80_red, minimum=-3, maximum=3, byres=1

#make a pretty figure
create ca_obj, 1RVX_trimer_correctnumbering and name ca
ramp_new ramp_obj, ca_obj, [-3,3], [-1,-1,0]
set surface_color, ramp_obj, 1RVX_trimer_correctnumbering
show_as surface, ca_obj
hide everything, 1RVX_trimer_correctnumbering
delete ramp_obj
set ray_shadow, off
set ray_opaque_background, off
ray 2400,2400
