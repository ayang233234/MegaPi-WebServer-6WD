from flask import Flask
import urllib3
from abc import ABCMeta, abstractmethod
from megapi import *

PowerModule = MegaPi()
server = Flask(__name__)

class FourWheelDriveCar():
    # 支持六个车轱辘

    def __init__(self):
        self.MotorReset()
        self.Servoinit()

    # config = configparser.ConfigParser()
    # config.read("config.ini")
    # self.LEFT_1 = config.getint("car", "LEFT_1")

    # 重置
    # 舵机角度初始化
    def Servoinit(self):
        PowerModule.servoRun(8, 1, 90)
        PowerModule.servoRun(8, 1, 90)
        PowerModule.servoRun(8, 2, 90)
        PowerModule.servoRun(8, 2, 90)
        PowerModule.servoRun(7, 1, 90)
        PowerModule.servoRun(7, 1, 90)
        PowerModule.servoRun(7, 2, 90)
        PowerModule.servoRun(7, 2, 90)
        PowerModule.servoRun(6, 1, 90)
        PowerModule.servoRun(6, 1, 90)
        PowerModule.servoRun(6, 2, 90)
        PowerModule.servoRun(6, 2, 90)

        # 将所有电机速度清零

    def MotorReset(self):
        PowerModule.motorRun(1, 0)
        PowerModule.motorRun(9, 0)
        PowerModule.motorRun(2, 0)
        PowerModule.motorRun(10, 0)
        PowerModule.motorRun(3, 0)
        PowerModule.motorRun(11, 0)

    # 前进
    def forward(self):
        self.MotorReset()
        PowerModule.motorRun(1, 50)
        PowerModule.motorRun(9, 50)
        PowerModule.motorRun(2, 50)
        PowerModule.motorRun(10, 50)
        PowerModule.motorRun(3, 50)
        PowerModule.motorRun(11, 50)

    # 后退
    def backward(self):
        self.MotorReset()
        PowerModule.motorRun(1, -50)
        PowerModule.motorRun(9, -50)
        PowerModule.motorRun(2, -50)
        PowerModule.motorRun(10, -50)
        PowerModule.motorRun(3, -50)
        PowerModule.motorRun(11, -50)

    # 左转
    def turnLeft(self):
        self.MotorReset()
        LeftInitAngle = 90
        LeftAngle = LeftInitAngle + 5
        PowerModule.servoRun(8, 1, LeftAngle)

        PowerModule.servoRun(8, 2, LeftAngle)

        PowerModule.servoRun(7, 1, LeftAngle)

        PowerModule.servoRun(7, 2, LeftAngle)

        PowerModule.servoRun(6, 1, LeftAngle)

        PowerModule.servoRun(6, 2, LeftAngle)

    # 右转
    def turnRight(self):
        self.MotorReset()
        RightInitAngle = 90
        RightAngle = RightInitAngle - 5
        PowerModule.servoRun(8, 1, RightAngle)

        PowerModule.servoRun(8, 2, RightAngle)

        PowerModule.servoRun(7, 1, RightAngle)

        PowerModule.servoRun(7, 2, RightAngle)

        PowerModule.servoRun(6, 1, RightAngle)

        PowerModule.servoRun(6, 2, RightAngle)

    def stop(self):
        self.MotorReset()
        self.Servoinit()

@server.route("/car/control/<int:act>",methods=["GET"])
def car_control(act:int):
    if act == 1:
        car.forward()  # 参数1为前进
        return 1
    if act == 2:
        car.backward()  # 参数2为后退
        return 1
    if act == 3:
        car.turnLeft()  # 参数3为左转
        return 1
    if act == 4:
        car.turnRight()  # 参数4为右转
        return 1
    if act == 0:
        car.stop()  # 参数0为停车
        return 1
    else:
        return -1



if __name__ == "__main__":
    PowerModule.start('/dev/ttyUSB0')
    car = FourWheelDriveCar()
    PORT_NUM = 8899  # 后端监听端口
    server.run(port=PORT_NUM, debug=True)
    car.stop() 
    print('Exit...')
