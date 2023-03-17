from djitellopy import Tello
from time import sleep
import cv2

# setarea obiectului tello
tello = Tello()
tello.connect()
print(tello.get_battery())

# setarea fiselor de misiuni
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)

# initializarea captarii imaginii la calculator
tello.streamon()

tello.takeoff()
pad = tello.get_mission_pad_id()


def takePicture():
    cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
    sleep(0.5)

def imageCapture():
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (480, 360))
    cv2.imshow("Image", img)
    cv2.waitKey(1)


def moveToMissionPad():
    imageCapture()
    pad = tello.get_mission_pad_id()
    sleep(0.05)
    print(pad)
    sleep(0.05)
    tello.send_rc_control(0, 10, 0, 0)
    sleep(0.05)


while pad != 2:
    moveToMissionPad()
tello.send_rc_control(0, 0, 0, 0)
takePicture()
tello.rotate_clockwise(90)

while pad != 3:
    moveToMissionPad()
tello.send_rc_control(0, 0, 0, 0)
takePicture()
tello.rotate_clockwise(90)

while pad != 4:
    moveToMissionPad()
tello.send_rc_control(0, 0, 0, 0)
takePicture()
tello.rotate_clockwise(90)

while pad != 1:
    moveToMissionPad()
tello.send_rc_control(0, 0, 0, 0)
takePicture()
tello.rotate_clockwise(90)

tello.land()
