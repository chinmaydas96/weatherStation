from getTime import getTime
from data import gtime

while True:
        dtime = getTime()
        temp = getTemp()
        with open("data.tsv","a") as myfile:
                myfile.write(dtime  +"\t" +str(temp) +"\n")
~                                                               
