from djitellopy import Tello
from time import sleep

#crearea obiectului tello si conectarea dronei

tello = Tello()
tello.connect()

#configurarea dronei pentru fisele de misiune

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)

# decolarea dronei
tello.takeoff()
pad = tello.get_mission_pad_id()

while pad != 5:
    print(pad)
    sleep(3)

tello.land()