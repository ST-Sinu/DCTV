import cv2
import ditel
#from fall_detector3 import FallDetector
import djitellopy as tello
from time import sleep
#import Keyboard
import keyboard_controller as kc
import threading
import multiprocessing as mp

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

def fall_start(drone,fall_detector):
    fall_detector.begin(drone)

if __name__ == '__main__':
    drone_state = False
    #fall_detector = FallDetector()
    drone = tello.Tello()
    fallstate = False

    if drone_state == False:                #연결 시 dronse_state = True로 
        drone_state = drone_connect(drone)
    drone.streamon()

    keyboard_controller = kc.TelloKeyboardController(drone)
    # process_fall = mp.Process(target=fall_start,args=(drone,fall_detector))
    # process_fall.start()
    # process_fall.join()
      

while 1:
    if drone.stream_on:
        drone_img1 = drone.get_frame_read().frame
        result_img1 = ditel.dino(drone_img1)
        cv2.imshow("knife",result_img1)
        key = cv2.waitKey(1)
        threading.Thread(target=tello_control, args=(key, keyboard_controller)).start() 
            # if fallstate == False:
            #     threading.Thread(target=fall_start,args=(drone,fall_detector)).start()
            #     fallstate = True
    else:
        quit()

    #드론 조종하는 코드
    # key = cv2.waitKey(1)
    # threading.Thread(target=tello_control, args=(key, keyboard_controller)).start()