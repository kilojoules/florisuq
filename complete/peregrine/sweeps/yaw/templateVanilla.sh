#!/bin/bash
#PBS -l walltime=4:00:00
#######PBS -l walltime=4:00:00
#PBS -l nodes=2
######PBS -q debug
#PBS -q short
#PBS -A windse
. ~/bears/bin/activate
for WS in WS_VALUE
do
  for jj in WS_STD
  do
      for DIR in DIR_VALUE
      do
         cp ../* .
         sed -i "s/STD_DIR/${ii}/g" sweepvanilla.in
         sed -i "s/STD_WS/${jj}/g" sweepvanilla.in
         sed -i "s/WSVAL/${WS}/g" example_input.json
         sed -i "s/WSVAL/${WS}/g" sweepvanilla.in
         sed -i "s/DIR/${DIR}/g" example_input.json
         dakota -i sweepvanilla.in
         cp dakota_tabular.dat ../data/WS_${WS}_dir_${DIR}_dstd${ii}_wstd${jj}.dat
      done
   done
done
