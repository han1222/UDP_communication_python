## download teleop-twist-joy
    sudo apt-get install ros-melodic-teleop-twist-joy
## execution order
    roscore   
    roslaunch teleop_twist_joy teleop.launch
    rostopic echo /joy
    python udp_client_dict.py
    python udp_server_dict.py
