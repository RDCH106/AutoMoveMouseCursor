# -*- coding: utf-8 -*-

from metadata import Metadata


class Messages:

    @staticmethod
    def print_wellcome():
        meta = Metadata()
        print("    ___         __           __  ___               ")
        print("   /   | __  __/ /_____     /  |/  /___ _   _____  ")
        print("  / /| |/ / / / __/ __ \   / /|_/ / __ \ | / / _ \ ")
        print(" / ___ / /_/ / /_/ /_/ /  / /  / / /_/ / |/ /  __/ ")
        print("/_/  |_\__,_/\__/\____/  /_/  /_/\____/|___/\___/  ")
        print(" ______________________________________________________")
        print("/_____/_____/_____/_____/_____/_____/_____/_____/_____/  v" + meta.get_version())
        print("    __  ___                         ______                          ")
        print("   /  |/  /___  __  __________     / ____/_  ________________  _____")
        print("  / /|_/ / __ \/ / / / ___/ _ \   / /   / / / / ___/ ___/ __ \/ ___/")
        print(" / /  / / /_/ / /_/ (__  )  __/  / /___/ /_/ / /  (__  ) /_/ / /    ")
        print("/_/  /_/\____/\__,_/____/\___/   \____/\__,_/_/  /____/\____/_/     ")
        print(" __________________________________________________________________")
        print("/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/")
        print("\n *Keep open during your game session \n\n")

    @staticmethod
    def print_shorcuts():
        print("-------------------------------------------------------------")
        print("Ctrl + m -> Move cursor to dead zone (screen bottom center)")
        print("Ctrl + p -> Move cursor to dead zone point (screen center)")
        print("Ctrl + d -> Activate/Deactivate debug mode")
        print("-------------------------------------------------------------")
        print("\n\n")
