jj=1
#for WS_VALUE in 5.0 6.0 7.0 8.0 9.0 10.0 11.0 12.0 13.0 14.0 15.0
for WS_VALUE in 3.0 4.0
do
   #for DIR_VALUE in -16 -14 -12 -10 -8 -6 -4 4 8 10 12 14 16 20
    for DIR_VALUE in  -20  
   do
      #for DIR_STD in 6. 7. 8. 9. 11. 12. 13. 14.
      for DIR_STD in 1. 2. 3. 4. 5. 6. 7. 8. 9. 10. 11. 12. 13. 14. 15.
      do
            #if [ $jj -gt 500 ] ; then  jj=1 ; fi
            mkdir working$jj ; cd working$jj
            cp ../* .
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
