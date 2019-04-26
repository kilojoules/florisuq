#!/bin/bash
#PBS -l walltime=20:00:00
#######PBS -l walltime=4:00:00
#PBS -l nodes=2
######PBS -q debug
#PBS -q batch-h
#PBS -A windse
. /scratch/jquick/sunflowers/bin/activate
for WS in WS_VALUE
do
  #for ii in 0
  #for ii in 8. 10. # dir std
  #for ii in 2. 
  for ii in 10 15
  #for ii in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
  do
     for jj in WS_STD
     #for jj in  .5 1. 2. # WS std
     do
         #for DIR in -20  -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 39 40
         for DIR in DIR_VALUE
         #for DIR in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40  -20  -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
         #for DIR in -20  -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
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
       
            cp ../example_optimization.py .
            sed -i "s/THESTATE/True/g" example_optimization.py
            dakota -i sweep.in
            mv dakota_tabular.dat 1.dat
            cp ../example_optimization.py .
            sed -i "s/THESTATE/False/g" example_optimization.py
            dakota -i sweep.in ok
            mv dakota_tabular.dat 2.dat
            python ps.py
            cp dakota_tabular.dat ../data/WS_${WS}_dir_${DIR}_dstd${ii}_wstd${jj}.dat
            #cd ..
         done
      done
   done
done
  
rm -rf $PWD
