from djitellopy import Tello

class TelloKeyboardController:
    def __init__(self, drone: Tello, in_flight = False):
        self.tello = drone
        self.in_flight = in_flight

    def control(self, key):
        if key == ord('w'):
            self.tello.move_forward(20)
            print("foward\n")
        elif key == ord('s'):
            self.tello.move_back(20)
        elif key == ord('a'):
            self.tello.move_left(20)
        elif key == ord('d'):
            self.tello.move_right(20)
        elif key == ord('e'):
            self.tello.rotate_clockwise(20)
        elif key == ord('q'):
            self.tello.rotate_counter_clockwise(20)
        elif key == ord('r'):
            self.tello.move_up(20)
        elif key == ord('f'):
            self.tello.move_down(20)
        elif key == ord(' '):
            if not self.in_flight:
                # Take-off drone
                self.tello.takeoff()
                self.in_flight = True
            elif self.in_flight:
                # Land tello 
                self.tello.land()
                self.in_flight = False
        elif key == 27: #esc
            self.tello.end()
        elif key == ord('p'):
            self.tello.send_rc_control(0, 0, 0, 0)