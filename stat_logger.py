def read_stat(s):
    f = open("/home/pi/solar_automa/stats/"+s, "r")
    return f.read()

def write_stat(data, file):
	f = open("stats/"+file, "w")
	f.write(str(data))
	f.close()