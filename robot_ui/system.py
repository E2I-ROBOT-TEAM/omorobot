# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:26:24 2025

@author: Cha
"""

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtGui import QColor


variable1=1
variable2=2


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 폴더에 위치해야한다.
form_class = uic.loadUiType("direction.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.resize(800, 600)
        
        #버튼에 기능을 연결하는 코드(객체.시그널.시그널과 슬롯을 연결.(슬롯))
        self.forward.pressed.connect(self.forwardbutton)
        self.forward.released.connect(self.stop)
        
        self.back.pressed.connect(self.backbutton)
        self.left.pressed.connect(self.leftbutton)
        self.right.pressed.connect(self.rightbutton)
        
        
        
    def stop(self) :
        
     
        
    #로봇 전진
    def forwardbutton(self) :
        
        
        while True :
            import serial
            ser = serial.Serial(
            port='COM6',\
            baudrate=115200)
                
            ser.write(b'$cVW,50,50\r\n') #출력방식2
        
        
            ser.close()
    
            #self.Textbrowser이름.append()
            #QTextbrowser에 글자를 추가하는 메서드
            self.textB.append("%dm/s, %d" %(variable1, variable2))  #로봇에서 받아온 값 표시
            
            
            
            
        
    #로봇 후진
    def backbutton(self) :
        
        import serial
        ser = serial.Serial(
        port='COM6',\
        baudrate=115200)

        ser.write(b'$cVW,-200,-200\r\n') #출력방식2
        
        
        ser.close()
    
        #self.Textbrowser이름.append()
        #QTextbrowser에 글자를 추가하는 메서드
        self.textB.append("%dm/s, %d" %(variable1, variable2))

    #로봇 좌회전
    def leftbutton(self) :
        
        import serial
        ser = serial.Serial(
        port='COM6',\
        baudrate=115200)

        ser.write(b'$cDIFFV,0,200\r\n') #출력방식2
        
        
        ser.close()
    
        #self.Textbrowser이름.append()
        #QTextbrowser에 글자를 추가하는 메서드
        self.textB.append("%dm/s, %d" %(variable1, variable2))
        
    #로봇 우회전
    def rightbutton(self) :
        
        import serial
        ser = serial.Serial(
        port='COM6',\
        baudrate=115200)

        ser.write(b'$cDIFFV,200,0\r\n') #출력방식2
        
        
        ser.close()
    
        #self.Textbrowser이름.append()
        #QTextbrowser에 글자를 추가하는 메서드
        self.textB.append("%dm/s, %d" %(variable1, variable2))
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass()      #객체 = myWindow
    myWindow.show()
    app.exec_()  
    """
    












import socket
import sys
import serial
import time
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtGui import QColor
from PyQt5 import *
from PyQt5.QtWidgets import QLabel, QDial, QApplication, QWidget
import threading


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 폴더에 위치해야한다.
form_class = uic.loadUiType("direction.ui")[0]

# speed, go, back1 전역변수 
speed = 0
go = 0
back1 = 0
ip = '192.168.0.0'  # 로봇과 통신하는 컴퓨터의 현재 IPv4 주소를 입력해야 함

class WindowClass(QMainWindow, form_class, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(1500, 1400)

        
        """
        # 시리얼 포트 열기
        try:
            #self.ser = serial.Serial(port='COM6', baudrate=115200, timeout=1)  # COM6 포트 사용, 타임아웃 1초
            
            
            #---------------------------------------------------------------
            
            port2 = 2346

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            '''while(1):
                message = input("message입력:")
                client_socket.sendto(message.encode("UTF-8"),(ip,port2))'''

            message=b'$cVW,100,100\r\n'
            client_socket.sendto(message,(ip,port2))
            
            #---------------------------------------------------------------
            
            port3 = 2347

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            '''while(1):
                message = input("message입력:")
                client_socket.sendto(message.encode("UTF-8"),(ip,port3))'''

            message=b'$cVW,100,100\r\n'
            client_socket.sendto(message,(ip,port3))
            
            #---------------------------------------------------------------
            
            port4 = 2348

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            '''while(1):
                message = input("message입력:")
                client_socket.sendto(message.encode("UTF-8"),(ip,port4))'''

            message=b'$cVW,100,100\r\n'
            client_socket.sendto(message,(ip,port4))
            
        except serial.SerialException as e:
            print(f"Serial Error: {e}")
            self.ser = None  # 시리얼 연결 실패 시 None 처리
        """
        

        # 타이머 설정 (버튼이 눌린 동안 계속 명령을 반복해서 보내기)
        self.timer = QTimer(self)  # 시간의 경과를 체크할 수 있는 객체를 설정함
        self.timer.setInterval(200)  # 타이머 간격을 200ms로 설정함
        self.timer.timeout.connect(self.send_move_command)  # 타이머가 실행될 때마다 함수 호출
        
        
        # QDial 작동 관련 타이머
        self.timers = QTimer(self)  # 시간의 경과를 체크할 수 있는 객체를 설정함
        self.timers.setInterval(50)  # 타이머 간격을 50ms로 설정함
        self.timers.timeout.connect(self.send_working_command)  # 타이머가 실행될 때마다 함수 호출
        

        self.ROBOT_moving = False  # 로봇이 움직이고 있는지 여부 (로봇 평소 상태)
        self.watch = False  # radio버튼 설정



        # 버튼 기능 연결
        self.forward.pressed.connect(self.forward_start)
        self.forward.released.connect(self.stop)

        self.back.pressed.connect(self.back_start)
        self.back.released.connect(self.stop)

        self.left.pressed.connect(self.left_start)
        self.left.released.connect(self.stop)

        self.right.pressed.connect(self.right_start)
        self.right.released.connect(self.stop)
        
        self.Exit_Communication.pressed.connect(self.Wireless_exit)
        
        
        #카메라 버튼 기능 연결
        self.camera_start.clicked.connect(self.startCamera)
        self.camera_stop.clicked.connect(self.stopCamera)
        
        
        # 카메라 상태 변수
        self.cap = None
        self.timer2 = QtCore.QTimer(self)
        self.timer2.timeout.connect(self.updateFrame)
        
        # UI 실행 시 카메라 자동 실행
        self.startCamera()
        
        
        # radio버튼 연결
        self.foward_radio.clicked.connect(self.radioFunction)
        self.backward_radio.clicked.connect(self.radioFunction)
        
      


        # 다이얼 시그널 연결
        self.speed_dial.valueChanged.connect(self.update_changed)
        self.speed_dial.valueChanged.connect(self.qtimes)
        self.speed_dial.sliderReleased.connect(self.stoped)
            

    # 다이얼 시그널 valueChanged 연결 함수 - QLabel에 값 표시
    def update_changed(self, getvalue):
        global speed
        speed = getvalue
        self.Dial_label.setText(f"{getvalue}")
        
        
     
    # radio 버튼 누를 때 호출되는 함수
    def radioFunction(self) :
        global speed
        global go
        global back1
        
        if self.foward_radio.isChecked() : 
            go = speed
            
        elif self.backward_radio.isChecked() : 
            back1 = speed    
        
            


    # 로봇에 명령 보내기
    #def send_serial_command(self, command):
        #if self.ser:
            #self.ser.write(command.encode())  # 시리얼로 명령 전송
            #time.sleep(0.2)  # 데이터 전송 후 잠시 대기 (버퍼 처리 및 하드웨어 반응 시간 고려)
            
    # 좌, 우, 전진, 후진 명령을 전송함
    def send_wireless_command_control(self, command1):
        global ip
        port1 = 1234  # 포트번호는 사용자가 4자리의 자연수로 임의로 설정하면 됨

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = command1
        client_socket.sendto(message,(ip,port1))
        
    # 로봇에 속도정보 확인명령을 전송함
    def send_wireless_command_velocity(self, command2):
        global ip
        port2 = 1235  # 포트번호는 사용자가 4자리의 자연수로 임의로 설정하면 됨

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = command2
        client_socket.sendto(message,(ip,port2))
        
   
    """
    # 로봇에서 속도 데이터 받아오기
    def get_serial_command(self, value):
        if self.ser:
            self.ser.write(value.encode())
            self.response = self.ser.readline().decode('utf-8').strip()
            time.sleep(0.2)
    """


    # 로봇이 이동 중일 때 계속해서 명령을 보냄
    def send_move_command(self):
         global go
         global back1
         
         if self.ROBOT_moving:
             if self.move_direction == 'forward':
                 #self.send_serial_command('$cVW,%d,%d\r\n' %(go, go))  # 통신명령에는 숫자만 들어갈 수 있음
                 self.send_wireless_command_control(b'$cVW,%d,%d\r\n' %(go, go))  # 통신명령에는 숫자만 들어갈 수 있음
                 self.send_wireless_command_velocity(b'$qDIFFV,%d,%d\r\n')
                 self.textB.append(f"Forward: {0}m/s")
                 
             elif self.move_direction == 'backward':
                 #self.send_serial_command('$cVW,%d,%d\r\n' %(-back1, -back1))
                 self.send_wireless_command_control(b'$cVW,%d,%d\r\n' %(-back1, -back1))  # 통신명령에는 숫자만 들어갈 수 있음
                 self.textB.append("Backward: -200m/s, -200")
             elif self.move_direction == 'left':
                 #self.send_serial_command('$cDIFFV,-50,50\r\n')
                 self.send_wireless_command_control(b'$cDIFFV,%d,%d\r\n' %(-50, 50))  # 통신명령에는 숫자만 들어갈 수 있음
                 self.textB.append("Left Turn: -100m/s, 100")
             elif self.move_direction == 'right':
                 #self.send_serial_command('$cDIFFV,50,-50\r\n')
                 self.send_wireless_command_control(b'$cDIFFV,%d,%d\r\n' %(50, -50))  # 통신명령에는 숫자만 들어갈 수 있음
                 self.textB.append("Right Turn: 100m/s, -100")
                
    
    def send_working_command(self) :
        if self.watch :
            if self.work == 'working' :
                self.radioFunction()
                
                
    def Wireless_exit(self):
        self.send_wireless_command_control(b"1111")
       

    
    
        

    def forward_start(self):
        self.ROBOT_moving = True
        self.move_direction = 'forward'
        self.timer.start()  # 타이머 시작

    def back_start(self):
        self.ROBOT_moving = True
        self.move_direction = 'backward'
        self.timer.start()  # 타이머 시작

    def left_start(self):
        self.ROBOT_moving = True
        self.move_direction = 'left'
        self.timer.start()  # 타이머 시작

    def right_start(self):
        self.ROBOT_moving = True
        self.move_direction = 'right'
        self.timer.start()  # 타이머 시작

    def stop(self):
        self.ROBOT_moving = False
        self.timer.stop()  # 타이머 종료
        #self.send_serial_command('$cVW,0,0\r\n')  # 로봇 멈추기
        self.send_wireless_command('$cVW,0,0\r\n')
        self.textB.append("Stop: 0m/s, 0")
        
    
    # QDial 실시간 조작 종료
    def stoped(self):
        self.watch = False
        self.timers.stop()  # 타이머 종료
        
        
    # QDial 실시간 타이머
    def qtimes(self):
        self.watch = True
        self.work = 'working'
        self.timers.start()

    """
    def closeEvent(self, event):
        if self.ser:
            self.ser.close()  # 프로그램 종료 시 시리얼 포트 닫기
        event.accept()
    """  
        


        

        
    # 카메라 실행 (자동 실행 혹은 버튼 클릭 시 실행)
    def startCamera(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)  # 기본 카메라 사용
            if not self.cap.isOpened():
                QtWidgets.QMessageBox.about(self, "Error", "카메라를 열 수 없습니다.")
                self.cap = None
                return
            self.timer2.start(30)  # 30ms마다 updateFrame 실행
            
            
    # 카메라 프레임 업데이트 (QTimer 이용)
    def updateFrame(self):
        ret, img = self.cap.read()
        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.camera_label.setPixmap(pixmap)
   
        
   # 카메라 정지
    def stopCamera(self):
        if self.cap is not None:
            self.timer2.stop()  # 타이머 중지
            self.cap.release()
            self.cap = None
        self.camera_label.clear()
        

    
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()



    

  
   
      

        
        
        
        
      
        
        
    