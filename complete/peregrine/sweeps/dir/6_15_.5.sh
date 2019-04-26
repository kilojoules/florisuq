#!/bin/bash
#PBS -l walltime=4:00:00
#######PBS -l walltime=4:00:00
#PBS -l nodes=1
######PBS -q debug
#PBS -q short
#PBS -A windse
#for WS in 10. #12.
for WS in 8.0
do
  #for ii in 0
  #for ii in 8. 10. # dir std
  #for ii in 2. 
  for ii in 15.
  do
     for jj in .5
     #for jj in  .5 1. 2. # WS std
     do
         for DIR in -5 #-4 -3 -2 -1 0 1 2 3 4 5 6 8 10 12 14 16 18 20
         #for DIR in -10  -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
         do
            mkdir working1 ; cd working1
            #mkd WS_${WS}_dir_${DIR}_dstd${ii}_wstd${jj}
            cp ../* .
            sed -i "s/STD_DIR/${ii}/g" sweep.in
            sed -i "s/STD_WS/${jj}/g" sweep.in
            sed -i "s/WSVAL/${WS}/g" example_input.json
            sed -i "s/WSVAL/${WS}/g" sweep.in
            sed -i "s/DIR/${DIR}/g" example_input.json
            dakota -i sweep.in
            #qsub run.pbs
            #mv dakota_tabular.dat ../data/WS_${WS}_dir_${DIR}_dstd${ii}_wstd${jj}.dat
            cp dakota_tabular.dat ../data/WS_${WS}_dir_${DIR}_dstd${ii}_wstd${jj}.dat
            cd ..
         done
      done
   done
done
  
