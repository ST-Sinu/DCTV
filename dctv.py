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

def drone_connect(drone):
    connection = False
    try:
        drone.connect()
        connection = True
    except Exception as e:
        connection = False
    return connection

if __name__ == '__main__':
    drone_state = False
    fall_detector = FallDetector()
    drone = tello.Tello()
    
    if drone_state == False:                #연결 시 dronse_state = True로 
        drone_state = drone_connect(drone)

    drone_vid = drone.streamon()
    keyboard_controller = kc.TelloKeyboardController(drone)
    fall_detector.begin(drone_vid)
    key = cv2.waitKey(1)
    threading.Thread(target=tello_control, args=(key, keyboard_controller)).start()



#while 1:
    # if drone.stream_on:
    #     drone_img1 = drone.get_frame_read().frame
    #     #drone_img2 = drone_img1
    #     result_img1 = ditel.dino(drone_img1)
    #     #result_img2 = fall_detector.begin(drone_img2)
    #     cv2.imshow("knife",result_img1)
    #     #cv2.imshow("fall",result_img2)
    # else:
    #     quit()

    #드론 조종하는 코드
    # key = cv2.waitKey(1)
    # threading.Thread(target=tello_control, args=(key, keyboard_controller)).start()