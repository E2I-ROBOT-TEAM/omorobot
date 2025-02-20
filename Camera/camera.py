import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap

class CameraWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        # 카메라 상태 변수
        self.cap = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        
        # UI 실행 시 카메라 자동 실행
        self.startCamera()
    
    def initUI(self):
        """UI 구성"""
        self.setWindowTitle("Camera Viewer")
        
        # 카메라 화면 출력 QLabel
        self.camera_label = QLabel(self)
        self.camera_label.setFixedSize(640, 480)
        
        # 카메라 시작 버튼
        self.camera_start = QPushButton("Start Camera", self)
        self.camera_start.clicked.connect(self.startCamera)
        
        # 카메라 정지 버튼
        self.camera_stop = QPushButton("Stop Camera", self)
        self.camera_stop.clicked.connect(self.stopCamera)
        
        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.camera_label)
        layout.addWidget(self.camera_start)
        layout.addWidget(self.camera_stop)
        self.setLayout(layout)
    
    def startCamera(self):
        """카메라 실행"""
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)  # 기본 카메라 사용
            if not self.cap.isOpened():
                print("Error: 카메라를 열 수 없습니다.")
                self.cap = None
                return
            self.timer.start(30)  # 30ms마다 updateFrame 실행
    
    def updateFrame(self):
        """카메라 프레임 업데이트 (QTimer 이용)"""
        ret, img = self.cap.read()
        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.camera_label.setPixmap(pixmap)
    
    def stopCamera(self):
        """카메라 정지"""
        if self.cap is not None:
            self.timer.stop()  # 타이머 중지
            self.cap.release()
            self.cap = None
        self.camera_label.clear()
    
    def closeEvent(self, event):
        """프로그램 종료 시 카메라 정리"""
        self.stopCamera()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cameraWindow = CameraWidget()
    cameraWindow.show()
    sys.exit(app.exec_())