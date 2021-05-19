
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urllib3
from abc import ABCMeta, abstractmethod
import time
#import configparser
from megapi import *

PowerModule = MegaPi()

class FourWheelDriveCar():
    # 支持六个车轱辘
 
    def __init__(self):
                self.MotorReset()
                self.Servoinit()
        #config = configparser.ConfigParser()
        #config.read("config.ini")
        #self.LEFT_1 = config.getint("car", "LEFT_1")
        


 #重置
        #舵机角度初始化
    def Servoinit(self):
        PowerModule.servoRun(8,1,90)
        PowerModule.servoRun(8,1,90)
        PowerModule.servoRun(8,2,90)
        PowerModule.servoRun(8,2,90)
        PowerModule.servoRun(7,1,90)
        PowerModule.servoRun(7,1,90)
        PowerModule.servoRun(7,2,90)
        PowerModule.servoRun(7,2,90)
        PowerModule.servoRun(6,1,90)
        PowerModule.servoRun(6,1,90)
        PowerModule.servoRun(6,2,90)
        PowerModule.servoRun(6,2,90)



        #将所有电机速度清零
    def MotorReset(self):
        PowerModule.motorRun(1,0)
        PowerModule.motorRun(9,0)
        PowerModule.motorRun(2,0)
        PowerModule.motorRun(10,0)
        PowerModule.motorRun(3,0)
        PowerModule.motorRun(11,0)
#前进
    def _forward(self):
        self.MotorReset()
        PowerModule.motorRun(1,50)
        PowerModule.motorRun(9,50)
        PowerModule.motorRun(2,50)
        PowerModule.motorRun(10,50)
        PowerModule.motorRun(3,50)
        PowerModule.motorRun(11,50)
#后退 
    def _backward(self):
        self.MotorReset()
        PowerModule.motorRun(1,-50)
        PowerModule.motorRun(9,-50)
        PowerModule.motorRun(2,-50)
        PowerModule.motorRun(10,-50)
        PowerModule.motorRun(3,-50)
        PowerModule.motorRun(11,-50)
 #左转
    def _turnLeft(self):
        self.MotorReset()
        LeftInitAngle = 90
        LeftAngle = LeftInitAngle + 5
        PowerModule.servoRun(8,1,LeftAngle)

        PowerModule.servoRun(8,2,LeftAngle)

        PowerModule.servoRun(7,1,LeftAngle)

        PowerModule.servoRun(7,2,LeftAngle)

        PowerModule.servoRun(6,1,LeftAngle)

        PowerModule.servoRun(6,2,LeftAngle)
#右转
    def _turnRight(self):
        self.MotorReset()
        RightInitAngle = 90
        RightAngle = RightInitAngle - 5
        PowerModule.servoRun(8,1,RightAngle)

        PowerModule.servoRun(8,2,RightAngle)

        PowerModule.servoRun(7,1,RightAngle)

        PowerModule.servoRun(7,2,RightAngle)

        PowerModule.servoRun(6,1,RightAngle)

        PowerModule.servoRun(6,2,RightAngle) 


    def _stop(self):
        self.MotorReset()
        self.Servoinit()

class DispatcherHandler(BaseHTTPRequestHandler):
        def do_GET(self):
                print('client:', self.client_address, 'reuest path:', self.path,
                                'command:', self.command)
                #query = urllib.splitquery(self.path)
                query= self.path.split('?', 1)
                action = query[0]
                params = {}
                if len(query) == 2:
                        for key_value in query[1].split('&'):
                                kv = key_value.split('=')
                                if len(kv) == 2:
                                        params[kv[0]] = urllib3.unquote(kv[1]).decode("utf-8", "ignore")
                runCar = RunCar()
                print(params)
                buf = {}
                if self.path.startswith("/car?"):
                        buf["return"] = runCar.action(params)
                else:
                        buf["return"] = -1
                self.protocal_version = "HTTP/1.1"
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=UTF-8")
                #self.send_header("Content-type", "test/html; charset=UTF-8")
                self.send_header("Pragma", "no-cache")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(buf)

        def do_POST(self):
                self.send_error(404)

class Job():
        __metaclass__ = ABCMeta
        @abstractmethod
        def action(self, params):
                pass

      #创建一个公类，跑起来吧(｡・`ω´･)           
class RunCar(Job):
        car = FourWheelDriveCar()
        def action(self, params):
                print(params)
                act = int(params['a']) #将参数强制为实型，避免未知错误。
                if act == 1:
                        self.car._forward() #参数1为前进
                        return 1
                if act == 2:
                        self.car._backward() #参数2为后退
                        return 1
                if act == 3:
                        self.car._turnLeft() #参数3为左转
                        return 1
                if act == 4:
                        self.car._turnRight() #参数4为右转
                        return 1
                if act == 0:
                        self.car._stop() #参数0为停车
                        return 1
                else:
                        return -1 

if __name__ == "__main__":
        PowerModule.start('/dev/ttyUSB0')
        PORT_NUM = 8899 #后端监听端口
        serverAddress = ("", PORT_NUM)
        server = HTTPServer(serverAddress, DispatcherHandler)
        print('Started httpserver on port: ', PORT_NUM)
        try:
                server.serve_forever()
        except KeyboardInterrupt as e:
                pass
        finally:
                MotorReset()
                Servoinit()
                server.socket.close()

                print('Exit...')