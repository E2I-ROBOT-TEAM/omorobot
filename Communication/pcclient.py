#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading
import time

ip = '192.168.1.19'
port = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def DataReceive():
    while True:
        client_socket.sendto(b'',(ip,port))
        modifiedMessage, serverAddress = client_socket.recvfrom (2048)
        print(modifiedMessage)
        time.sleep(1)
    

thread = threading.Thread(target=DataReceive)
thread.start()


message=b'$cVW,100,100\r\n'
client_socket.sendto(message,(ip,port))

modifiedMessage, serverAddress = client_socket.recvfrom (2048)
print(modifiedMessage)

def close():
    client_socket.close()
    print("연결종료")

