import sys
lastline = None
lastlastline = None
for line in open('dak.out', 'r').readlines():
   if lastlastline:
      if 'Mean' in lastlastline: 
         val = (line.split()[1])
         break
   lastlastline = lastline
   lastline = line
outf = open('%s.exp' % sys.argv[-1], 'w')
outf.write(str(val) + '\n')
outf.close()
