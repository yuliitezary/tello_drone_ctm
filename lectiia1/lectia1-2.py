from djitellopy import Tello

tello = Tello()
tello.connect()
print(tello.get_battery())

tello.takeoff()

tello.move_forward(50)
tello.rotate_clockwise(360)
tello.move_left(50)
tello.rotate_clockwise(360)
tello.move_back(50)
tello.rotate_clockwise(360)
tello.move_right(50)
tello.rotate_clockwise(360)
tello.move_forward(20)


tello.land()
