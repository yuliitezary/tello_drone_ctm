from djitellopy import Tello

tello = Tello()
tello.connect()
print(tello.get_battery())

tello.takeoff()

tello.move_forward(50)

tello.flip_left()
tello.flip_right()


tello.land()
