import socket

ip = '192.168.1.19'
port = 2345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message=b'$cVW,100,100\r\n'
client_socket.sendto(message,(ip,port))

def close():
    client_socket.close()
    print("연결종료")
