jj=1
for WS_VALUE in 6.0 8.0 10.0 12.0
do
   for DIR_VALUE in -16 -14 -12 -10 -8 -6 -4 -2 0 2 4 8 10 12 14 16 20
   do
         if [ $jj -gt 12 ] ; then  jj=1 ; fi
         mkdir working$jj ; cd working$jj
         cp ../* .
         Fil=${WS_VALUE}_${DIR_VALUE}_${DIR_STD}_${WS_STD}.sh
         cp templateVanilla.sh $Fil
         sed -i "s/WS_VALUE/$WS_VALUE/" $Fil
         sed -i "s/DIR_VALUE/$DIR_VALUE/" $Fil
         qsub $Fil
         cd ..
         ((jj++))
   done
done
