import socket
import time
from matplotlib import pyplot as plt

receive_address = '0.0.0.0'
receive_port = 50001

in_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

listening_address = (receive_address, receive_port)

in_sock.bind(listening_address)

x_axis = [0 for i in range(100)]
y_axis_sensor_l = [0 for i in range(100)]
y_axis_sensor_c = [0 for i in range(100)]
y_axis_sensor_r = [0 for i in range(100)]

plt.ylim(0, 2500)
plt.grid()

now_time = time.time()
start_time = now_time

line_l, =  plt.plot(x_axis, y_axis_sensor_l, color='#ff0000')
line_c, =  plt.plot(x_axis, y_axis_sensor_c, color='#00ff00')
line_r, =  plt.plot(x_axis, y_axis_sensor_r, color='#0000ff')

plt.xlabel("Time")
plt.ylabel("Sensor Value")
plt.title("Sensors Data Graph")

while True:
    in_bytes, client_address = in_sock.recvfrom(128)
    in_data = in_bytes.decode("utf-8")
    data_array = in_data.split(",")

    if data_array[0] == "log":
        x_axis.pop(0)
        x_axis.append(int(now_time - start_time))

        y_axis_sensor_l.pop(0)
        y_axis_sensor_l.append(int(data_array[1]))

        y_axis_sensor_c.pop(0)
        y_axis_sensor_c.append(int(data_array[2]))

        y_axis_sensor_r.pop(0)
        y_axis_sensor_r.append(int(data_array[3]))

        plt.xlim(min(x_axis), max(x_axis))

        line_l.set_xdata(x_axis)
        line_l.set_ydata(y_axis_sensor_l)

        line_c.set_xdata(x_axis)
        line_c.set_ydata(y_axis_sensor_c)

        line_r.set_xdata(x_axis)
        line_r.set_ydata(y_axis_sensor_r)

    plt.pause(0.0001)

    now_time = time.time()

    print(in_data)
