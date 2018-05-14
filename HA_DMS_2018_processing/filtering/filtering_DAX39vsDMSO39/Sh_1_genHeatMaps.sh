
# First take RepN_xxx.txt, remove the first line (header) to create data_repN.txt in directory repN
# Change output file name accordingly in the python template, copy the python file to directory repN
# In directory repN, run python


# For nomutfile, need to open for example, LIB1_countsAAcodons.xlsx in Excel, remove the last line, and save it as Widows formatted text file LIB1_countsAAcodons.txt

name="DAX39_mutdiffsel.txt"

nrep=3
nres=565

pythontemplate=Py_heatmap_template_v2.py

gnuplottemplate=Gnuplot_heatmap.gplt

for ((n=1; n<=$nrep; n++)); do
  title="DAX39 mutdiffsel rep${n}"
  rawfile=Rep${n}_${name}
  datafile=data_rep${n}.txt
  pythonfile=Py_heatmap_rep${n}.py
  nomutfile=LIB${n}_countsAAcodons.txt
  dir=rep$n

  mkdir $dir

  ntmp=`cat $rawfile | wc -l`
  nline=$(($ntmp-1))
  echo $ntmp, $nline
  tail -$nline $rawfile > $dir/$datafile

  sed -e "s/var_nres/$nres/g; s/outfile/out_heatmap_rep$n/g" $pythontemplate > $dir/$pythonfile
  cp $nomutfile $dir/
  #nline=$(($nres+1))
  #head -$nline $nomutfile $dir/$nomutfile #remove the last line; only head nres+1 line

  ires=0
  fres=$res  
  var_ytics=50
  gnuplotfile=Gnuplot_heatmap_rep${n}_all.gplt
  sed -e "s/var_ytics/${var_ytics}/g; s/var_ires/0/g; s/var_fres/${nres}/g; s/infile/out_heatmap_rep$n/g; s/outfile/out_heatmap_rep${n}_all/g; s/var_title/$title/g" $gnuplottemplate > $dir/$gnuplotfile
  for ((j=0; j<=4; j++)); do
    ires=$(($j*100))
    fres=$(($ires+100))  
    var_ytics=5
    gnuplotfile=Gnuplot_heatmap_rep${n}_${ires}_${fres}.gplt
    sed -e "s/var_ytics/${var_ytics}/g; s/var_ires/${ires}/g; s/var_fres/${fres}/g; s/infile/out_heatmap_rep$n/g; s/outfile/out_heatmap_rep${n}_${ires}_${fres}/g; s/var_title/$title/g" $gnuplottemplate > $dir/$gnuplotfile
  done
  ires=500
  fres=$nres  
  var_ytics=5
  gnuplotfile=Gnuplot_heatmap_rep${n}_${ires}_${fres}.gplt
  sed -e "s/var_ytics/${var_ytics}/g; s/var_ires/${ires}/g; s/var_fres/${nres}/g; s/infile/out_heatmap_rep$n/g; s/outfile/out_heatmap_rep${n}_${ires}_${fres}/g; s/var_title/$title/g" $gnuplottemplate > $dir/$gnuplotfile


  cp labels_aa.txt $dir
  cd $dir
     python $pythonfile $datafile $nomutfile
     gnuplotfile=Gnuplot_heatmap_rep${n}_all.gplt
     gnuplot << EOF
       load '$gnuplotfile'
EOF
     for ((j=0; j<=4; j++)); do
       ires=$(($j*100))
       fres=$(($ires+100))  
       gnuplotfile=Gnuplot_heatmap_rep${n}_${ires}_${fres}.gplt
       gnuplot << EOF
         load '$gnuplotfile'
EOF
     done
     ires=500
     fres=$nres  
     gnuplotfile=Gnuplot_heatmap_rep${n}_${ires}_${fres}.gplt
     gnuplot << EOF
       load '$gnuplotfile'
EOF

     for file in *.eps; do
       filename=`ls $file | cut -f 1 -d '.'`
       echo "process $filename"
       epstopdf $filename.eps
     done

  cd ..

done

