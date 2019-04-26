#!/bin/bash
#PBS -l walltime=44:00:00
#######PBS -l walltime=4:00:00
#PBS -l nodes=3:ppn=20
######PBS -q debug
#PBS -q batch-h
#PBS -A windse
. /scratch/jquick/sunflowers/bin/activate
for WS in WS_VALUE
do
  #for ii in 0
  #for ii in 8. 10. # dir std
  #for ii in 2. 
  for ii in DIR_STD
  do
     for jj in WS_STD
     #for jj in  .5 1. 2. # WS std
     do
         #for DIR in DIR_VALUE
         #for DIR in 0 1 2 3 4 5 -5 -4 -3 -2 -1 6 7 8 9 10 11 12 13 14 15 
         #for DIR in -10  -9 -8 -7 -6 -5 -4 -3 -2 -1
         for DIR in -40 -39 -38 -37 -36 -35 -34 -33 -32 -31 -30 -29 -28 -27 -26 -25 -24 -23 -22 -21 -20  -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
         #for DIR in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
         #for DIR in -10  -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
         do
            #mkdir working1 ; cd working1
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
            #cd ..
         done
      done
   done
done
  
