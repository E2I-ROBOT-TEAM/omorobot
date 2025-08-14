#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 00:22:20 2025

@author: kensMACbook
"""

import time
import serial
import struct
import numpy as np


class KYDLidar:
    def __init__(self, port="/dev/tty.usbserial-0001", baudrate=230400):
        self.ser = serial.Serial(port, baudrate)
        
    def start_scan(self):
        """라이다 시작 명령"""
        self.ser.write(bytes([0xA5, 0x60]))
        time.sleep(0.1)
        
    def stop_scan(self):
        """라이다 정지 및 시리얼 종료"""
        self.ser.write(bytes([0xA5, 0x65]))
        self.ser.close()
        
    def parse_sample(self, si_bytes):
        s0, s1, s2 = si_bytes
        distance = (s2 << 6) + (s1 >> 2)
        intensity = s1 + ((s2 & 0x03) * 256)
        return distance, intensity

    def calc_angle(self, index, lsn, fsa, lsa):
        angle_fsa = (fsa >> 1) / 64.0
        angle_lsa = (lsa >> 1) / 64.0
        if lsn <= 1:
            return angle_fsa
        diff = angle_lsa - angle_fsa
        return angle_fsa + (diff * index / (lsn - 1))

    def angle_correction(self, distance):
        if distance == 0:
            return 0.0
        return np.degrees(np.arctan((21.8 * (155.3 - distance)) / (155.3 * distance)))
    
    def read_packet(self):
        # 헤더 탐색
        while True:
            if self.ser.read(1) == b'\xAA' and self.ser.read(1) == b'\x55':
                break

        ct = self.ser.read(1)
        lsn = struct.unpack('B', self.ser.read(1))[0]
        fsa = struct.unpack('<H', self.ser.read(2))[0]
        lsa = struct.unpack('<H', self.ser.read(2))[0]
        cs = self.ser.read(2)
        samples = self.ser.read(lsn * 3)
        distance = np.zeros(lsn)
        intensity = np.zeros(lsn)
        angle = np.zeros(lsn)

        for i in range(lsn):
            si = samples[i*3:(i+1)*3]
            if len(si) < 3:
                continue

            distance[i], intensity[i] = self.parse_sample(si)
            angle[i] = self.calc_angle(i, lsn, fsa, lsa)
            angle[i] += self.angle_correction(distance[i])
            
        return distance, intensity, angle
    
    
if __name__ == "__main__":
    lidar = KYDLidar()
    lidar.start_scan()
    try:
        while True:
            dis,intensity,angle = lidar.read_packet()
            print(dis,intensity,angle)
            
    except KeyboardInterrupt:
        lidar.stop_scan()
        print("\n[중단] 사용자 종료")
    finally:
        lidar.stop_scan()
