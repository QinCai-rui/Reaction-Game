"""
/***************************************************************
 *                                                             *
 *                    GNU GENERAL PUBLIC LICENSE               *
 *                       Version 3, 29 June 2007               *
 *                                                             *
 *  Copyright (c) 2024 by Raymont Qin. https://qincai.xyz      *
 *  Licensed under the GPLv3 license                           *
 *                                                             *
 *  This program is free software: you can redistribute it and *
 *  or modify it under the terms of the GNU General Public     *
 *  License as published by the Free Software Foundation,      *
 *  either version 3 of the License, or (at your option) any   *
 *  later version.                                             *
 *                                                             *
 *  This program is distributed in the hope that it will be    *
 *  useful, but WITHOUT ANY WARRANTY; without even the implied *
 *  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR    *
 *  PURPOSE. See the GNU General Public License for more       *
 *  details.                                                   *
 *                                                             *
 *  You should have received a copy of the GNU General Public  *
 *  License along with this program. If not, see               *
 *  <https://www.gnu.org/licenses/>.                           *
 *                                                             *
 ***************************************************************/
"""

from machine import Pin, I2C
from random import randint
import ssd1306
from time import sleep, ticks_ms, ticks_diff

# Initialise the LED
LED = Pin("LED", Pin.OUT)

# Initialise the buttons
BTN_L = Pin(0, Pin.IN, Pin.PULL_UP)
BTN_R = Pin(11, Pin.IN, Pin.PULL_UP)

# VDD for OLED display
oled_VDD = Pin(18, Pin.OUT, value = 1)

# Initialise I2C for the SSD1306 OLED display
i2c = I2C(0, scl=Pin(17), sda=Pin(16))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


# Function for testing the build
def test():
    LED.value(1)
    sleep(2)
    LED.value(0)
    
    # Clear the display
    oled.fill(0)
    oled.text("TEST", 0, 0)
    oled.show()
  
    while 1:
        if BTN_R.value() == 0:
            LED.value(1)
            sleep(1)
        LED.value(0)


def test2():
    while 1:
        print(BTN_R.value())
        sleep(0.1)


# Function that asks for the mode of game
def select_mode():
    global singleMode
    oled.fill(0)
    oled.text("Select Mode", 0, 0)
    oled.show()
    sleep(1)
    oled.text("L btn: 1 player", 0, 20)
    oled.show()
    sleep(1)
    oled.text("R btn: 2 players", 0, 30)
    oled.show()
    sleep(0.5)
    while 1:
        if BTN_L.value() == 0:
            singleMode = True
            break
        if BTN_R.value() == 0:
            singleMode = False
            break

    if singleMode: 
        mode = '1-player mode'
    else: 
        mode = '2-player mode'

    oled.fill(0)
    oled.text("Mode you chose: ", 0, 0)
    oled.text(f"{mode}", 0, 10) 
    oled.show()
    sleep(2.5)

    mode_loading()


# Function to load the game mode
def mode_loading():
    if singleMode:
        single_game_loop()
    else:
        duo_game_loop()


# Funtion to be called when someone cheats
def anti_cheating(player):
    LED.value(0)
    if player == "single":  # If cheated in single player mode...
        oled.fill(0)
        oled.text("Uh uh!", 0, 0)
        oled.text("No cheating!", 0, 10)

    elif player == "duo1":   # If cheated in double player mode...
        oled.fill(0)
        oled.text("Uh uh!", 0, 0)
        oled.text("No cheating PL1!", 0, 10)

    elif player == "duo2":   # If cheated in double player mode...
        oled.fill(0)
        oled.text("Uh uh!", 0, 0)
        oled.text("No cheating PL2!", 0, 10)

    oled.show()
    sleep(1.25)
    oled.text("Please release", 0, 20)
    oled.show()
    sleep(0.85)
    oled.text("the buttons and", 0, 30)
    oled.show()
    sleep(0.85)
    oled.text("restart the game", 0, 40)
    oled.show()
    sleep(2.5)
    oled.fill(0)
    oled.show()
    while BTN_L.value() == 0 or BTN_R.value() == 0:
        pass
    sleep(2)
    # Hard reset
    import machine; machine.reset()
        

# Function to print reaction time on screen
def print_reaction_time(reactionTime, mode):
    if reactionTime < 10000:
        if mode == "single":
            oled.text(f"time was {reactionTime}ms!", 0, 10)
        elif mode == "duo":
            oled.text(f"time was {reactionTime}ms!", 0, 20)
            
    elif reactionTime < 100000:
        reactionTime /= 1000
        reactionTime = round(reactionTime, 2)
        if mode == "single":
            oled.text(f"time was {reactionTime}s!", 0, 10)
        elif mode == "duo":
            oled.text(f"time was {reactionTime}s!", 0, 20)
            
    else:
        if mode == "single":
            oled.text("time was 100+ s", 0, 10)
        elif mode == "duo":
            oled.text("time was 100+ s", 0, 20)
        

# Game loop for a single person
def single_game_loop(): 
    # This block of code prints the intro on the OLED screen
    oled.fill(0)
    oled.text("Welcome! In this", 0, 0)
    oled.show()
    sleep(0.85)
    oled.text("mode of the game", 0, 10)
    oled.show()
    sleep(0.85)
    oled.text("you aim to press", 0, 20)
    oled.show()
    sleep(0.85)
    oled.text("the button", 0, 30)
    oled.show()
    sleep(0.85)
    oled.text("as soon as the", 0, 40)
    oled.show()
    sleep(0.85)
    oled.text("LED turns off...", 0, 50)
    oled.show()
    sleep(2)
    oled.fill(0)
    oled.text("The game will", 0, 0)
    oled.show()
    sleep(0.85)
    oled.text("now start. The", 0, 10)
    oled.show()
    sleep(0.85)
    oled.text("LED should light", 0, 20)
    oled.show()
    sleep(0.85)
    oled.text("up now. Have fun", 0, 30)
    oled.show()
    sleep(2)
    # END

    # Turns the LED on
    LED.value(1)

    # Clears the OLED screen
    oled.fill(0)
    oled.show()

    timeLED_off = int(ticks_ms()) + int((1000 * (randint(5,10))))
    
    while not timeLED_off == ticks_ms():
        if BTN_L.value() == 0:  # If button is pressed before LED turns off...
            anti_cheating("single")

    # Turns off the LED and starts the timer
    LED.value(0)
    startTime = ticks_ms()

    # Now wait for the button press after the LED turns off
    global reactionTime
    while True:
        if BTN_L.value() == 0:
            pressTime = ticks_ms()
            reactionTime = ticks_diff(pressTime, startTime)
            break
            
    # Clears the screen and prints the congrats message
    oled.fill(0)
    oled.text("Your reaction", 0, 0)
    print_reaction_time(reactionTime, "single")
    oled.show()
    sleep(3)
    oled.text("To play again, ", 0, 30)
    oled.show()
    sleep(0.85)
    oled.text("just restart the", 0, 40)
    oled.text("program!", 0, 50)
    oled.show()


# Game loop for two people
def duo_game_loop():
    # This block of code prints the intro on the OLED screen
    oled.fill(0)
    oled.text("Welcome! In this", 0, 0)
    oled.show()
    sleep(0.85)
    oled.text("game, you aim to", 0, 10)
    oled.show()
    sleep(0.85)
    oled.text("press your btn", 0, 20)
    oled.show()
    sleep(0.85)
    oled.text("ASAP after the", 0, 30)
    oled.show()
    sleep(0.85)
    oled.text("LED turns off...", 0, 40)
    oled.show()
    sleep(3.5)
    oled.fill(0)
    oled.text("The game will", 0, 0)
    oled.show()
    sleep(0.5)
    oled.text("now start.", 0, 10)
    oled.show()
    sleep(0.85)
    oled.text("Rmbr to press", 0, 20)
    oled.show()
    sleep(0.85)
    oled.text("your btn before", 0, 30)
    oled.show()
    sleep(0.85)
    oled.text("your opponent!", 0, 40)
    oled.show()
    sleep(2.5)
    oled.text("LED is on!", 0, 50)
    oled.show()
    sleep(1)
    # END

    # Turns the LED on
    LED.value(1)

    # Clears the OLED screen
    oled.fill(0)
    oled.show()

    timeLED_off = int(ticks_ms()) + int((1000 * (randint(5,10))))
    
    while not timeLED_off == ticks_ms():
        if BTN_L.value() == 0:  # If left button is pressed before LED turns off...
            anti_cheating("duo1")
        elif BTN_R.value() == 0:  # If right button is pressed before LED turns off...
            anti_cheating("duo2")
    
    # Turns off the LED and starts the timer
    LED.value(0)
    startTime = ticks_ms()

    # Now wait for the button press after the LED turns off
    global reactionTime
    while True:
        if BTN_L.value() == 0 or BTN_R.value() == 0:
            pressTime = ticks_ms()
            reactionTime = ticks_diff(pressTime, startTime)
            if BTN_L.value() == 0:
                winner = 1
            elif BTN_R.value() == 0:
                winner = 2
            break
    
    # Clears the screen and prints the congrats message
    oled.fill(0)
    if winner == 1:
        oled.text("Left player won!", 0, 0)
    elif winner == 2:
        oled.text("Right player won", 0, 0)
    oled.show()
    sleep(1.5)
    oled.text("Their reaction", 0, 10)
    print_reaction_time(reactionTime, "duo")
    oled.show()
    sleep(3)
    oled.text("To play again, ", 0, 30)
    oled.show()
    sleep(0.85)
    oled.text("just restart the", 0, 40)
    oled.text("program!", 0, 50)
    oled.show()


def main():
    for i in range(10):
        LED.value(1)
        sleep(0.0625)
        LED.value(0)
        sleep(0.0625)
    select_mode()


if __name__ == "__main__":
    try: 
        main()
    except Exception:
        oled.fill(0)
        oled.show()
        LED.value(0)
