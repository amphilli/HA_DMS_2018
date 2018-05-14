
# First take RepN_xxx.txt, remove the first line (header) to create data_repN.txt in directory repN
# Change output file name accordingly in the python template, copy the python file to directory repN
# In directory repN, run python

name="DAX39_mutdiffsel.txt"

nrep=3
nres=565

data1=out_heatmap_rep1.txt
data2=out_heatmap_rep2.txt
data3=out_heatmap_rep3.txt
pythonfile=Py_compare_heatmaps_v6.py
python $pythonfile $data1 $data2 $data3

gnuplottemplate=Gnuplot_3heatmaps.gplt
infile=out_heatmaps_all3
title="DAX39 mutdiffsel"
ires=0
fres=$res  
var_ytics=50
gnuplotfile=Gnuplot_3heatmaps_all.gplt
sed -e "s/var_ytics/${var_ytics}/g; s/var_ires/${ires}/g; s/var_fres/${nres}/g; s/infile/$infile/g; s/outfile/out_heatmaps_all3_all/g; s/var_title/$title/g" $gnuplottemplate > $gnuplotfile
gnuplot << EOF
       load '$gnuplotfile'
EOF

# plot heatmaps of the three replicas in the same fig

for ((j=0; j<=4; j++)); do
  ires=$(($j*100))
  fres=$(($ires+100))  
  var_ytics=5
  gnuplotfile=Gnuplot_3heatmaps_${ires}_${fres}.gplt
  sed -e "s/var_ytics/${var_ytics}/g;s/var_ires/${ires}/g; s/var_fres/${fres}/g; s/infile/$infile/g; s/outfile/out_heatmaps_all3_${ires}_${fres}/g; s/var_title/$title/g" $gnuplottemplate > $gnuplotfile
  gnuplot << EOF
       load '$gnuplotfile'
EOF

done

ires=500
fres=$nres  
var_ytics=5
gnuplotfile=Gnuplot_3heatmaps_${ires}_${fres}.gplt
sed -e "s/var_ytics/${var_ytics}/g; s/var_ires/${ires}/g; s/var_fres/${nres}/g; s/infile/$infile/g; s/outfile/out_heatmaps_all3_${ires}_${fres}/g; s/var_title/$title/g" $gnuplottemplate > $gnuplotfile
gnuplot << EOF
       load '$gnuplotfile'
EOF

# plot pickout heatmap

gnuplottemplate=Gnuplot_heatmap_pickout.gplt
infile=out_heatmaps_pickouts
ires=0
fres=$res
var_ytics=50
gnuplotfile=Gnuplot_heatmap_pickout_all.gplt
sed -e "s/var_ytics/${var_ytics}/g; s/var_ires/0/g; s/var_fres/${nres}/g; s/infile/$infile/g; s/outfile/out_heatmap_pickouts/g; s/var_title/$title/g" $gnuplottemplate > $gnuplotfile
gnuplot << EOF
       load '$gnuplotfile'
EOF

for ((j=0; j<=4; j++)); do
  ires=$(($j*100))
  fres=$(($ires+100))
  var_ytics=5
  gnuplotfile=Gnuplot_heatmap_pickout_${ires}_${fres}.gplt
  sed -e "s/var_ytics/${var_ytics}/g; s/var_ires/${ires}/g; s/var_fres/${fres}/g; s/infile/$infile/g; s/outfile/out_heatmap_pickouts_${ires}_${fres}/g; s/var_title/$title/g" $gnuplottemplate > $gnuplotfile
  gnuplot << EOF
       load '$gnuplotfile'
EOF
done


ires=500
fres=$nres
var_ytics=5
gnuplotfile=Gnuplot_heatmap_pickout_${ires}_${fres}.gplt
sed -e "s/var_ytics/${var_ytics}/g; s/var_ires/${ires}/g; s/var_fres/${nres}/g; s/infile/$infile/g; s/outfile/out_heatmap_pickouts_${ires}_${fres}/g; s/var_title/$title/g" $gnuplottemplate > $gnuplotfile
gnuplot << EOF
       load '$gnuplotfile'
EOF

for file in *.eps; do
  filename=`ls $file | cut -f 1 -d '.'`
  echo "process $filename"
  epstopdf $filename.eps
done

