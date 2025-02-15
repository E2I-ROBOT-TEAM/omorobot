#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import serial


ip = '192.168.1.222' #오모로봇 포트
port = 1234 

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((ip,port))

ser = serial.Serial(port = '/dev/ttyTHS1', baudrate =115200)

while(1):
    data, address = server_socket.recvfrom(1024)
    ser.write(data)
    print(data)
    if (data == b'1111'): #데이터로 1111을 보내면 정지
        break

server_socket.close()
