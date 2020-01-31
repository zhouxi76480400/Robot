import ev3dev.ev3 as ev3
import socket

import time

send_to_address = '172.16.10.157'
send_to_port = '50001'

ts = ev3.TouchSensor('in1')

mA = ev3.Motor('outA')
mD = ev3.Motor('outC')


def stop():
    mA.stop()
    mD.stop()


stop()

usL = ev3.UltrasonicSensor('in3')
usR = ev3.UltrasonicSensor('in2')
usC = ev3.UltrasonicSensor('in4')


def forward():
    mA.run_forever(duty_cycle_sp=50)
    mD.run_forever(duty_cycle_sp=50)


def back():
    mA.run_forever(duty_cycle_sp=-50)
    mD.run_forever(duty_cycle_sp=-50)


def left():
    mA.run_forever(duty_cycle_sp=-50)
    mD.run_forever(duty_cycle_sp=50)


def right():
    mA.run_forever(duty_cycle_sp=50)
    mD.run_forever(duty_cycle_sp=-50)


out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

now_fresh_time = time.time()

try:
    while ts.value() == 0:
        value_usl = usL.value()
        value_usc = usC.value()
        value_usr = usR.value()

        forward()
        time.sleep(0.1)
        if value_usc < 300:
            back()
            time.sleep(1)
            left()
            time.sleep(1)
        if value_usl < 300:
            right()
            time.sleep(1)
        if value_usr < 300:
            left()
            time.sleep(1)
    # send data to pc
        now_time = time.time()
        if now_time - now_fresh_time >= 1:
            print("aaaa")
            now_fresh_time = now_time
            
except KeyboardInterrupt:
    stop()
    
stop()
