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

# Initialise the on-board LED
LED = Pin("LED", Pin.OUT)

# Initialise the buttons
BTN_L = Pin(0, Pin.IN, Pin.PULL_UP)
BTN_R = Pin(11, Pin.IN, Pin.PULL_UP)

# VDD for OLED display
oled_VDD = Pin(18, Pin.OUT, value=1)

# Initialise I2C for the SSD1306 OLED display
i2c = I2C(0, scl=Pin(17), sda=Pin(16))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


# Function for testing the LED and OLED screen
def test():
    LED.value(1)
    sleep(2)
    LED.value(0)

    # Clear the display
    oled.fill(0)
    oled.text("TEST", 0, 0)
    oled.show()


# Function to test the buttons
def test2():
    while 1:
        print(BTN_L.value())
        print(BTN_R.value())
        sleep(0.125)


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
        mode = "1-player mode"
    else:
        mode = "2-player mode"

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

    elif player == "duo1":  # If cheated in double player mode...
        oled.fill(0)
        oled.text("Uh uh!", 0, 0)
        oled.text("No cheating PL1!", 0, 10)

    elif player == "duo2":  # If cheated in double player mode...
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
    import machine

    machine.reset()


# Function to print reaction time on screen
def print_reaction_time(reactionTime, mode):
    if reactionTime < 10000:
        if mode == "single":
            oled.text(f"time: {reactionTime}ms", 0, 10)
        elif mode == "duo":
            oled.text(f"time: {reactionTime}ms", 0, 20)
    elif reactionTime < 100000:
        reactionTime /= 1000
        reactionTime = round(reactionTime, 2)
        if mode == "single":
            oled.text(f"time: {reactionTime}s", 0, 10)
        elif mode == "duo":
            oled.text(f"time: {reactionTime}s", 0, 20)
    else:
        if mode == "single":
            oled.text("time: 100+ s", 0, 10)
        elif mode == "duo":
            oled.text("time: 100+ s", 0, 20)

    oled.show()
    sleep(1)
    feedback1, feedback2 = provide_feedback(reactionTime)
    oled.text(feedback1, 0, 30)
    oled.text(feedback2, 0, 40)
    oled.show()


# Function to provide feedback based on reaction time
def provide_feedback(reactionTime):
    if reactionTime < 20:
        feedback1 = "You are faster"
        feedback2 = "than a cat!"
    elif reactionTime < 50:
        feedback1 = "You are as quick"
        feedback2 = "as a cat!"
    elif reactionTime < 70:
        feedback1 = "You have lightni"
        feedback2 = "ng-fast reflexes"
    elif reactionTime < 100:
        feedback1 = "You are reflexiv"
        feedback2 = "e like a ninja!"
    elif reactionTime < 150:
        feedback1 = "You are sooo"
        feedback2 = "fast!"
    elif reactionTime < 200:
        feedback1 = "You are quicker"
        feedback2 = "than most!"
    elif reactionTime < 250:
        feedback1 = "You are quite"
        feedback2 = "fast!"
    elif reactionTime < 300:
        feedback1 = "You are average."
        feedback2 = ""  # Not needed
    elif reactionTime < 400:
        feedback1 = "You are slower"
        feedback2 = "than average."
    elif reactionTime < 500:
        feedback1 = "You need a bit"
        feedback2 = "more practice."
    elif reactionTime < 700:
        feedback1 = "You are really"
        feedback2 = "taking your time!"
    elif reactionTime < 2000:
        feedback1 = "You might need"
        feedback2 = "more coffee."
    else:
        feedback1 = "Are you using"
        feedback2 = "this as a timer?"
    return feedback1, feedback2


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
    # Turns the LED on
    LED.value(1)
    oled.text("up now. Have fun", 0, 30)
    oled.show()
    sleep(2)
    # END

    # Clears the OLED screen
    oled.fill(0)
    oled.show()

    timeLED_off = int(ticks_ms()) + int((1000 * (randint(5, 10))))

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
    sleep(2.5)
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
    sleep(2)
    # Turns the LED on
    LED.value(1)
    oled.text("LED is on!", 0, 50)
    oled.show()
    sleep(1)
    # END

    # Clears the OLED screen
    oled.fill(0)
    oled.show()

    timeLED_off = int(ticks_ms()) + int((1000 * (randint(5, 10))))

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


if __name__ == "__main__":
    try:
        select_mode()
    except KeyboardInterrupt:
        oled.fill(0)
        oled.show()
        LED.value(0)
