# for WS in 5.0
#for WS in 4.0
#for WS in 8.0
#for WS in 9.0
for WS in 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 11.0 12.0 13.0 14.0 15.0
#for WS in 6.0 7.0 8.0 10.0 11.0 12.0 13.0 14.0 15.0
#for WS in 10.0
do
   #for DIR in 350
   for DIR in 350 340 330 320 310 300 0 10 20 30 40 50 60
   #for DIR in 60
   do
      mkdir ${WS}_$DIR
      cd ${WS}_$DIR
      cp ../* .
      sed -i "s/DIR/$DIR/" example_input.json
      sed -i "s/WS/$WS/" example_input.json
      sed -i "s/WS/$WS/" textbook_opt_ouu1.in 
      sed -i "s/WS/$WS/" uq2.in
      qsub run.pbs
      cd ..
   done
done
