# -*- coding: utf-8 -*-

from metadata import Metadata
import pyautogui
import keyboard
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
        self.__keyboard = keyboard.add_hotkey(hotkey="ctrl+m", callback=self.move_to_dead_zone)

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

    def move_to_dead_zone(self):
        print("Move Mouse Event: (%s,%s)" % (str(self.__screen_size[0]/2), str(self.__screen_size[1])))
        pyautogui.moveTo(self.__screen_size[0]/2, self.__screen_size[1])

    def run(self):
        while True:
            if self.in_area():
                if time.time() - self.__prev_timestamp > self.__timer:
                    self.move_to_dead_zone()
            else:
                self.__prev_timestamp = time.time()
            time.sleep(1)

    def print_wellcome(self):
        meta = Metadata()
        print("    ___         __           __  ___               ")
        print("   /   | __  __/ /_____     /  |/  /___ _   _____  ")
        print("  / /| |/ / / / __/ __ \   / /|_/ / __ \ | / / _ \ ")
        print(" / ___ / /_/ / /_/ /_/ /  / /  / / /_/ / |/ /  __/ ")
        print("/_/  |_\__,_/\__/\____/  /_/  /_/\____/|___/\___/  ")
        print(" ______________________________________________________")
        print("/_____/_____/_____/_____/_____/_____/_____/_____/_____/  v"+meta.get_version())
        print("    __  ___                         ______                          ")
        print("   /  |/  /___  __  __________     / ____/_  ________________  _____")
        print("  / /|_/ / __ \/ / / / ___/ _ \   / /   / / / / ___/ ___/ __ \/ ___/")
        print(" / /  / / /_/ / /_/ (__  )  __/  / /___/ /_/ / /  (__  ) /_/ / /    ")
        print("/_/  /_/\____/\__,_/____/\___/   \____/\__,_/_/  /____/\____/_/     ")
        print(" __________________________________________________________________")
        print("/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/")
        print("\n *Keep open during your game session \n\n")

if __name__ == "__main__":   # It is being run directly
    watcher = Watcher()
    watcher.print_wellcome()
    watcher.run()
