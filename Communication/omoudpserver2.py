#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time
import socket
import serial

Receivedata=b''

def DataReceive():
    while True:
        print('receiving')
        Receivedata=b''
        ser.write(b'$qPOSE\r\n')
        Receivedata=ser.readline()
        time.sleep(0.2)
    
    
thread = threading.Thread(target=DataReceive)
thread.start()




ip = '192.168.1.222' #omorobot ip
port = 1234 

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((ip,port))

ser = serial.Serial(port = '/dev/ttyTHS1', baudrate =115200)

while(1):
    data, address = server_socket.recvfrom(1024)
    ser.write(data)
    print(data)
    server_socket.sendto(Receivedata,address)
    if (data == b'1111'): #If you send 1111, it will stop
        break

server_socket.close()
