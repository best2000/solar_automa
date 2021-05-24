import socket, sys
print(sys.argv)
address = sys.argv[1]
message = sys.argv[2]

s = socket.socket()
#192.168.1.158 = vega56  sudo etherwake -i wlan0 2C:F0:5D:5A:34:AC
#192.168.1.152 = gtx970  sudo etherwake -i wlan0 E0:3F:49:A4:0C:00
s.connect((address, 2000))
s.sendall(message.encode('utf-8'))
print(s.recv(1024))
s.close()
