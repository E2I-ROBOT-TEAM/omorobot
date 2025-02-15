#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import serial
import time

ip = '192.168.0.0' 
port1 = 1234
port2 = 1235

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((ip,port1))
server_socket.bind((ip,port2))

ser = serial.Serial(port = '/dev/ttyTHS1', baudrate =115200)
print("수신 대기 중")

while(True):
    data, address = server_socket.recvfrom(1024)
    ser.write(data)
    print(data)
    if (data == b'1111'): 
        break

server_socket.close()

while True:
    time.sleep(1)
