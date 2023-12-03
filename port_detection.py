import socket

target_ip = '192.168.31.100'   # 目标主机的IP地址
target_ports = [7890, 7891,7892, 7893]   # 需要检测的目标端口列表

for port in target_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)   # 设置超时时间为1秒钟
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))
    sock.close()