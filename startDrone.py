from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()
print(tello.get_battery())

# decolarea dronei
tello.takeoff()

'''count = 4

while count > 0:
    tello.move('forward', 50)
    tello.rotate_clockwise(90)
    count = count - 1

'''

tello.send_rc_control(0,50,0,0)
sleep(2)
tello.send_rc_control(0,0,0,0)

#aterizarea dronei
tello.land()
