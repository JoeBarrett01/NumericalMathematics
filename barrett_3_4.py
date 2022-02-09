# Use file answers_13_4.txt as an output
# Just append that file!
# Feel free to change the name of variables MpSp, MpDp, SnSp, and SnDp

Name = "Joe Barrett"

#Machine Precision - Single Precision
from numpy import float32 

base = float32(2)
u = float32(1/2)
temp = 0
while (float32(1 + u)>float32(1)):
    temp = u
    u = u/base

#Machine Precision - Double Precision
from numpy import float64 

base = float64(2)
MpDp = float64(1/2)
temp = 0
while (float64(1 + MpDp)>float64(1)):
    temp = MpDp
    MpDp = MpDp/base
    
#Smallest Positive Number - Single Precision
from numpy import float32
base = float32(2)
temp = float32(1)
while (float32(temp) > float32(0)):
    SnSp = temp
    temp = temp/base

#Smallest Positive Number - Double Precision
base = 2
temp = 1
while (temp > 0):
    SnDp = temp
    temp = temp/base


fil=open("answers_13_4.txt","a+")
fil.write(Name + " " + "Machine precision for single precision is " + str(u) +"\n")
fil.write(Name + " " + "Machine precision for double precision is " + str(MpDp) + "\n")
fil.write(Name + " " + "Smallest positive number for single precision is " + str(SnSp) + "\n")
fil.write(Name + " " + "Smallest positive number for double precision is " + str(SnDp) + "\n")
fil.write("-----------------------------------------------\n\n")
fil.close()