# -*- coding: utf-8 -*-

import pyautogui
import time


class Watcher:

    def __init__(self):
        self.__prev_position = None
        self.__prev_timestamp = time.time()
        self.__timer = 5
        self.__screen_size = pyautogui.size()
        print("Screen Resolution: %sx%s" % (self.__screen_size[0], self.__screen_size[1]))
        self.__dead_zone_point = (960, 540)
        self.__dead_zone_radius = 50  # In pixels

    def in_area(self):
        pos = pyautogui.position()
        '''
         Function of belonging to a circle:
            (x - center_x)^2 + (y - center_y)^2 < radius^2

        '''
        # print(""
        #       + str((pos[0] - self.__dead_zone_point[0]) ** 2 + (pos[1] - self.__dead_zone_point[1]) ** 2)
        #       + " < "
        #       + str(self.__dead_zone_radius ** 2))
        if (pos[0] - self.__dead_zone_point[0]) ** 2 + (pos[1] - self.__dead_zone_point[1]) ** 2 \
                < self.__dead_zone_radius ** 2:
            return True
        else:
            return False

    def run(self):
        while True:
            if self.in_area():
                if time.time() - self.__prev_timestamp > self.__timer:
                    print("Move Mouse Event: (%s,%s)" % (str(self.__screen_size[0]),str(self.__screen_size[1])))
                    pyautogui.moveTo(self.__screen_size[0], self.__screen_size[1])
            else:
                self.__prev_timestamp = time.time()
            time.sleep(1)


if __name__ == "__main__":   # It is being run directly
    watcher = Watcher()
    watcher.run()
