#!/usr/bin/python3
import sys

file=open(sys.argv[1])
first=1
for l in file:
	if(l[0:1] != "["):
		if(l[0:1] != "/"):
			print(l,end='')
	else:
		if(first==1):
			first=0
		else:
			print(",",end='')
		f=l.split(",")
		print("%s,%s,%s,%s,%s]" % (f[0].replace(" ",""),f[2].replace(" ",""),f[4].replace(" ",""), f[5].replace(" ",""), f[13].replace(" ","")),end='')



#0 = 1         9- 14  I6    ---     HIP       Identifier (HIP number)                   (H1)
#1 = 5        42- 46  F5.2  mag     Vmag      ? Magnitude in Johnson V                  (H5)
#2 = 8        52- 63  F12.8 deg     RAdeg    *? alpha, degrees (ICRS, Epoch=J1991.25)   (H8)
#3 = 9        65- 76  F12.8 deg     DEdeg    *? delta, degrees (ICRS, Epoch=J1991.25)   (H9)
#4 = 37      246-251  F6.3  mag     B-V       ? Johnson B-V colour                     (H37)
