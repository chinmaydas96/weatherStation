from getTime import getTime
from getTemp import getTemp

while True:
        dtime = getTime()
        temp = getTemp()
        with open("data.tsv","a") as myfile:
                myfile.write(dtime  +"\t" +str(temp) +"\n")                                                               
