import Leap, sys, thread, time
from Leap import SwipeGesture

from Xlib import X, XK
from Xlib.display import Display
from Xlib.ext.xtest import fake_input

class GLeapListener(Leap.Listener):
    display = Display()
    last_time = 0

    def on_init(self, controller):
        print 'Initialized'

    def on_connect(self, controller):
        print 'Connected'
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        print 'Disconnected'

    def on_exit(self, controller):
        print 'Exited'

    def on_frame(self, controller):
        if (time.time() - self.last_time > 1):
            frame = controller.frame()

            for gesture in frame.gestures():
                if gesture.type == Leap.Gesture.TYPE_SWIPE:
                    swipe = SwipeGesture(gesture)
                    
                    self.last_time = time.time()
                    if (abs(swipe.direction[0]) > abs(swipe.direction[1])):
                        if (swipe.direction[0] > 0):
                            self.move_desktop(XK.XK_Left)
                        else:
                            self.move_desktop(XK.XK_Right)
                    else:
                        if (swipe.direction[1] > 0):
                            self.move_desktop(XK.XK_Down)
                        else:
                            self.move_desktop(XK.XK_Up)

    def move_desktop(self, direction):
        combo = (XK.XK_Alt_L, XK.XK_Control_L) + (direction,)
        for action in (X.KeyPress, X.KeyRelease):
            for keysym in combo:
                key = self.display.keysym_to_keycode(keysym)
                fake_input(self.display, action, key)
            self.display.sync()

def main():
    global listener
    global controller
    listener = GLeapListener()
    controller = Leap.Controller()
    controller.add_listener(listener)

if __name__ == '__main__':
    main()

while True:
    pass