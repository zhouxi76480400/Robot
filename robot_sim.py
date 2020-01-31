import socket
import time
import random


send_to_address = 'localhost'
send_to_port = 50001

# create a sock
out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def close():
    out_socket.close()


def rand():
    return random.randint(0, 2500)


def generate_fake_sensor_data():
    rand1 = rand()
    rand2 = rand()
    rand3 = rand()
    return "log,{0},{1},{2}".format(rand1, rand2, rand3)


last_refresh_time = time.time()

try:
    while True:
        now_time = time.time()
        if now_time - last_refresh_time >= 1:
            out_socket.sendto(generate_fake_sensor_data().encode("utf-8"), (send_to_address, send_to_port))
            last_refresh_time = now_time

except KeyboardInterrupt:
    close()

close()

