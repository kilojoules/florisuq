jj=1
#for WS_VALUE in 11.0 
#for WS_VALUE in 3.0 
for WS_VALUE in 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 11.0 12.0 13.0 14.0 15.0
#for WS_VALUE in 5.0 6.0 7.0 8.0 9.0 10.0 12.0 13.0 14.0 15.0
#for WS_VALUE in 8.0 9.0 10.0 11.0 12.0 13.0 14.0 15.0
do
   #for DIR_VALUE in 0
   for DIR_VALUE in -30 -29 -28 -27 -26 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
   do
      #for DIR_STD in 5
      #for DIR_STD in 5
      for DIR_STD in 1 
      #for DIR_STD in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
      #for DIR_STD in 0.10471976 0.12217305 0.13962634 0.15707963
      #for DIR_STD in 0.017453292519943295 0.03490658503988659 0.05235987755982989 0.06981317007977318 0.08726646259971647 0.17453292519943295 0.2617993877991494
      do
            #if [ $jj -gt 500 ] ; then  jj=1 ; fi
            mkdir working1_$jj ; cd working1_$jj
            cp ../template.sh .
            Fil=${WS_VALUE}_${DIR_VALUE}_${DIR_STD}.sh
            cp template.sh $Fil
            sed -i "s/WS_VALUE/$WS_VALUE/" $Fil
            sed -i "s/DIR_VALUE/$DIR_VALUE/" $Fil
            sed -i "s/DIR_STD/$DIR_STD/" $Fil
            qsub $Fil
            cd ..
            ((jj++))
       done
    done
done
