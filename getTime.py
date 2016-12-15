def getTime():

	import time
	data = time.ctime()
	raw = data.split(" ")[3]
	return raw
