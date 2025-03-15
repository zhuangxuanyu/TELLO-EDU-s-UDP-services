##此程序用于实时监视TELLO飞行器的各项飞行数据并输出##

import threading 
import socket
import sys
import time
import platform 
import re 

# 创建UDP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定到指定端口，IP设为0.0.0.0表示监听所有可用IP
server_address = ('0.0.0.0', 8890)
server_socket.bind(server_address)

def clear_previous_output(num_lines):
    ##使用 ANSI 转义序列清除之前的输出内容
    for _ in range(num_lines):
        sys.stdout.write("\033[F")  # 光标上移一行
        sys.stdout.write("\033[2K")  # 清除当前行
    sys.stdout.write("\r")
    sys.stdout.flush()

while True:
    data, address = server_socket.recvfrom(1024)
    ##print(f"{data.decode('utf-8')}") 
    message_string = data.decode('utf-8')                       # 输出的飞行器状态信息
    pattern = r'(\w+):(-?\d+\.?\d*)'                            # 使用正则表达式匹配键值对
    matches = re.findall(pattern, message_string)               
    data_dict = {key: float(value) for key, value in matches}   # 创建一个字典来存储键值对
    
    pitch = data_dict.get('pitch')
    roll = data_dict.get('roll')
    yaw = data_dict.get('yaw')
    vgx = data_dict.get('vgx')
    vgy = data_dict.get('vgy')
    vgz = data_dict.get('vgz')
    templ = data_dict.get('templ')
    temph = data_dict.get('temph')
    tof = data_dict.get('tof')
    h = data_dict.get('h')
    bat = data_dict.get('bat')
    baro = data_dict.get('baro')
    time_dr = data_dict.get('time')
    agx = data_dict.get('agx')
    agy = data_dict.get('agy')
    agz = data_dict.get('agz')
    
    
    clear_previous_output(11)                                    
    #各变量输出
    print(f"轴向姿态pitch: {pitch}")
    print(f"轴向姿态roll: {roll}")
    print(f"轴向姿态yaw: {yaw}")
    print(f"坐标速度vgx: {vgx}")
    print(f"坐标速度vgy: {vgy}")
    print(f"坐标速度vgz: {vgz}")
    print(f"主板最低温度templ: {templ}")
    print(f"主板最高温度temph: {temph}")
    print(f"传感器变化高度h: {h}")
    print(f"电池电量bat: {bat}")
    print(f"飞行时间timedr: {time_dr}")
    #print(f"{message}")