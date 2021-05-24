import socket, subprocess, logging

#logging.basicConfig(filename='stats/log', level=logging.DEBUG, format="%(asctime)s : %(message)s")
def message(addr, mess):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((addr, 2000))
		s.sendall(mess.encode('utf-8'))
		re = (s.recv(1024)).decode('utf-8')
		s.close()
		return re
	except:
		return None
		logging.warning("already sleep or maybe connection error!")

def wake(mac):
	subprocess.Popen("sudo etherwake -i wlan0 "+mac, shell=True)