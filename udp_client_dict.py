
import socket
import pickle

# Author: SEUNGIL HAN
# E-mail: robotics@kaist.ac.kr 


UDP_IP = "127.0.0.1" # write your Client IP Address local is 127.0.0.1
UDP_PORT = 5005 #port number

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print(pickle.loads(data))
    udp_dict = pickle.loads(data)
    print("longitudinal_cntrl_shock_level :", udp_dict["longitudinal_cntrl_shock_level"])
    print("udp_dict['lateral_cntrl_shock_level'] :", udp_dict["lateral_cntrl_shock_level"])

sock.close()
