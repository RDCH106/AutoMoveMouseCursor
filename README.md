# AutoMoveMouseCursor

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=contact@rdch106.hol.es&item_name=Donation&item_number=Software+Development&currency_code=EUR)

AutoMoveMouseCursor (AMMC) is a small application that allows you to move the mouse cursor over a region to a zone that does not disturb, if it does not move during a period of time. 

## Brief

AMMC is based on [AutoHidenMouseCursor](http://www.softwareok.com/?seite=Microsoft/AutoHideMouseCursor) concept, used to hide the mouse cursor in the PC games. It does not work with Steam Link device and the mouse is hidden to the PC screen but not to the Steam Link screen. An easy solution is move the cursor to the edge of the screen, but many games that use the mouse cursor to move the game camera reset the mouse position and put it in the middle of the screen. AMMC detect that the cursor is in the middle with constant position and move it to the bottom of the screen where is not visible. Each time that the cursor is detected during 5 seconds in the middle of the screen, AMMC will move it to the bottom of the screen.

**It is very usefull when games with controller compatibility show the mouse cursor in the menus, cutscenes or even in game.**

## How to use it?

Download the repository or clone it with:

`$ git clone https://github.com/RDCH106/AutoMoveMouseCursor`

Install [Python](https://www.python.org/downloads/) and then install the requirements with:

`$ pip install -r requirements.txt`

Execute it with:

`$ python auto_move_mouse_cursor.py`

And do not close it during your game session.

## Windows Binaries
### [Download latest release](https://github.com/RDCH106/AutoMoveMouseCursor/releases/latest)
