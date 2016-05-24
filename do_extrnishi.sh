#!/bin/bash -eu

mkdir -p ./result_coord


################################################################################
# function : bash
# description : 
################################################################################
file="prm.inp"
ex_quatnishi="./a.out"
iend=128
dir="/home/hnishi/4thTrial/ama2/md/md28"

#iend=`wc $file | cut -d' ' -f-10`
#iend=`wc -l $file | cut -d' ' -f 1`
#mkdir $dir/list_stru

echo total number of trajectories = $iend

#echo 74 > aaa.inp
#rm aaa.inp
 
rm coord_all.dat
touch coord_all.dat
for (( i=1; i<=$iend; i++ ))
do
   sed -e "s;mdx.crd;$dir/no$i/mdx.crd;" -e "s;coord.dat;./result_coord/coord.dat_$i;" $file > aaa
   $ex_quatnishi aaa > aaa.log
   cat ./result_coord/coord.dat_$i >> coord_all.dat
   wc -l coord_all.dat    
done

rm aaa aaa.log

echo end
#ls $dir/list_stru
