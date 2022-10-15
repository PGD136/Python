from ipaddress import ip_address
import socket

in_addr = socket.gethostbyname(socket.gethostname()) #gethostname = 내pc이름, 중간에 by주소

print(in_addr)