from flask import request, Flask, url_for, render_template
from threading import Timer

app = Flask(__name__)


def getTemp():
    temp_address = "/sys/bus/w1/devices/28-03160140daff/w1_slave"
    s = 1
    while s == 1:
        file = open(temp_address, "r")
        data = file.read()
        file.close()
        a = data.split()
        b = a[len(a) - 1]
        reading = b[2:]
        temp = float(reading) / 1000
        s = s + 1
        return temp


def getTime():
    import time
    data = time.ctime()
    raw = data.split(" ")[3]
    return raw


def data():
    dtime = getTime()
    temp = getTemp()
    with open("/static/data.tsv", "a") as myfile:
        myfile.write(dtime + "\t" + str(temp) + "\n")


@app.route('/data')
def work():
    t = Timer(1.00, data)
    return render_template('index.html')
    t.start()


if __name__ == '__main__':
    app.run(host='192.168.43.228')
