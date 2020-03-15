# -*- coding: utf-8 -*-

from messages import Messages
import pyautogui
import keyboard
import time


class Watcher:

    def __init__(self):
        self.__messages = Messages()
        self.__prev_position = None
        self.__prev_timestamp = time.time()
        self.__timer = 5
        self.__screen_size = pyautogui.size()
        print("Screen Resolution: %sx%s" % (self.__screen_size[0], self.__screen_size[1]))
        self.__dead_zone_point = (960, 540)
        self.__dead_zone_radius = 50  # In pixels
        self.__keyboard = keyboard.add_hotkey(hotkey="ctrl+m", callback=self.move_to_dead_zone)
        self.__debug = False
        self.__keyboard = keyboard.add_hotkey(hotkey="ctrl+d", callback=self.switch_debug)

    def in_area(self):
        pos = pyautogui.position()
        '''
         Function of belonging to a circle:
            (x - center_x)^2 + (y - center_y)^2 < radius^2

        '''
        if self.__debug:
            print("" +
                  str((pos[0] - self.__dead_zone_point[0]) ** 2 + (pos[1] - self.__dead_zone_point[1]) ** 2) +
                  " < " +
                  str(self.__dead_zone_radius ** 2))
        if (pos[0] - self.__dead_zone_point[0]) ** 2 + (pos[1] - self.__dead_zone_point[1]) ** 2 \
                < self.__dead_zone_radius ** 2:
            return True
        else:
            return False

    def move_to_dead_zone(self):
        print("Move Mouse Event: (%s,%s)" % (str(self.__screen_size[0]/2), str(self.__screen_size[1])))
        pyautogui.moveTo(self.__screen_size[0]/2, self.__screen_size[1])

    def switch_debug(self):
        self.__debug = not self.__debug
        if self.__debug:
            print("Debug Mode Activated!")
        else:
            print("Debug Mode Deactivated!")

    def run(self):
        while True:
            if self.in_area():
                if time.time() - self.__prev_timestamp > self.__timer:
                    self.move_to_dead_zone()
            else:
                self.__prev_timestamp = time.time()
            time.sleep(1)

    def print_wellcome(self):
        self.__messages.print_wellcome()

    def print_shorcuts(self):
        self.__messages.print_shorcuts()


if __name__ == "__main__":   # It is being run directly
    watcher = Watcher()
    watcher.print_wellcome()
    watcher.print_shorcuts()
    watcher.run()
