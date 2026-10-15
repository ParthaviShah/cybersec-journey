import socket
import sys
target=sys.argv[1]
for i in range(int(sys.argv[2]),int(sys.argv[3])):
	s=socket.socket()
	s.settimeout(3)
	result=s.connect_ex((target,i))
	if result==0:
		print(f"Port {i} is  open")
		try:
			banner=s.recv(1024)
			print(banner)
		except Exception as e :
			print(f"No banner received:{e}")
	s.close()
