from djitellopy import Tello

tello = Tello()
tello.connect()
print(tello.get_battery())

tello.takeoff()

tello.move_forward(50)
tello.move_left(50)
tello.move_back(50)
tello.move_right(50)
tello.move_up()
tello.move_down()

tello.rotate_clockwise()
tello.rotate_counter_clockwise()

tello.flip_back()
tello.flip_left()
tello.flip_right()
tello.flip_forward()

tello.land()
