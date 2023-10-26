import cv2
import ditel
from fall_detector import FallDetector
import djitellopy as tello
from time import sleep
#import Keyboard
import keyboard_controller as kc
import threading

def tello_control(key, keyboard_controller):
    keyboard_controller.control(key)

            
# def getInput():
#     left_right, front_back, up_down, clock_counter = 0, 0, 0, 0

#     if Keyboard.getkey("a"): left_right = -10
#     if Keyboard.getkey("d"): left_right = 10
#     if Keyboard.getkey("w"): front_back = 10
#     if Keyboard.getkey("s"): front_back = -10

#     if Keyboard.getkey("k"): up_down = 10
#     if Keyboard.getkey("l"): up_down = -10
#     if Keyboard.getkey("i"): clock_counter = -10
#     if Keyboard.getkey("o"): clock_counter = 10

#     if Keyboard.getkey("UP"): drone.takeoff()
#     if Keyboard.getkey("DOWN"): drone.land()

#     return [left_right, front_back, up_down , clock_counter]
in_flight = False
fall_detector = FallDetector()

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()
keyboard_controller = kc.TelloKeyboardController(drone)

while 1:
    drone_img = drone.get_frame_read().frame

    result_img1 = ditel.dino(drone_img)
    fall_detector.begin(drone)

    cv2.imshow("result_img1",result_img1)

    #드론 조종하는 코드
    # results = getInput()
    # if results != [0,0,0,0]:
    #     drone.send_rc_control(results[0],results[1],results[2],results[3])
    
    key = cv2.waitKey(1)
    if key == 27: # esc
        drone.streamoff()
        drone.land()
        drone.end()
        quit()
    elif key == 32:  # Space
            if not in_flight:
                # Take-off drone
                drone.takeoff()
                in_flight = True

            elif in_flight:
                # Land tello 
                drone.land()
                in_flight = False
    elif key == 112: #p
        drone.send_rc_control(0, 0, 0, 0)
        
    threading.Thread(target=tello_control, args=(key, keyboard_controller)).start()