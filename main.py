"""
/***************************************************************
 *                                                             *
 *                    GNU GENERAL PUBLIC LICENSE               *
 *                       Version 3, 29 June 2007               *
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
import time
import _thread

# Initialise the LED
LED = Pin(26, Pin.OUT)


# Initialise the buttons
BTN_L = Pin(19, Pin.IN, Pin.PULL_DOWN)
BTN_R = Pin(18, Pin.IN, Pin.PULL_DOWN)

# Initialise I2C for the SSD1306 OLED display
i2c = I2C(0, scl=Pin(17), sda=Pin(16))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


def test():
    LED.value(1)
    time.sleep(2)
    LED.value(0)
    
    # Clear the display
    oled.fill(0)
    oled.text("TEST", 0, 0)
    oled.show()
  
    while 1:
        if BTN_L.value() == 1:
            LED.value(1)
            time.sleep(1)
        LED.value(0)
        time.sleep(0.125)

def select_mode():
    global singleMode
    oled.fill(0)
    oled.text("Select Mode", 0, 0)
    oled.show()
    time.sleep(1)
    oled.text("L btn: 1 player", 0, 20)
    oled.show()
    time.sleep(1)
    oled.text("R btn: 2 players", 0, 30)
    oled.show()

    while 1:
        #global singleMode
        if BTN_L.value() == 1:
            singleMode = True
            break
        if BTN_R.value() == 1:
            singleMode = False
            break
        time.sleep(0.125)

    if singleMode: 
        mode = '1 player-mode'
    else: 
        mode = '2 player-mode'

    oled.fill(0)
    oled.text("Mode you chose: ", 0, 0)
    oled.text(f"{mode}", 0, 10) 
    oled.show()

    time.sleep(2.5)

    mode_loading()

def mode_loading():
    if singleMode:
        single_game_loop()
    else:
        duo_game_loop()

def anti_cheating_single():
    # Wait for the button to be released if it was pressed before the LED turned off
    if BTN_L.value() == 1:
        oled.fill(0)
        oled.text("Uh uh!", 0, 0)
        oled.text("No cheating!", 0, 10)
        oled.show()
        time.sleep(1.25)
        oled.text("Please release", 0, 20)
        oled.show()
        time.sleep(0.75)
        oled.text("the button and", 0, 30)
        oled.show()
        time.sleep(0.75)
        oled.text("try again. OR", 0, 40)
        oled.show()
        time.sleep(1.25)
        oled.text("restart the Pico", 0, 50)
        oled.show()
        time.sleep(2)
        oled.fill(0)
        oled.show()
        while BTN_L.value() == 1:
            time.sleep(0.001)

def single_game_loop(): 
    # This block of code prints the intro on the OLED screen
    oled.fill(0)
    oled.text("Welcome! In this", 0, 0)
    oled.show()
    time.sleep(0.75)
    oled.text("mode of the game", 0, 10)
    oled.show()
    time.sleep(0.75)
    oled.text("you aim to press", 0, 20)
    oled.show()
    time.sleep(0.75)
    oled.text("the button", 0, 30)
    oled.show()
    time.sleep(0.75)
    oled.text("as soon as the", 0, 40)
    oled.show()
    time.sleep(0.75)
    oled.text("LED turns off...", 0, 50)
    oled.show()
    time.sleep(2)
    
    oled.fill(0)
    oled.text("The game will", 0, 0)
    oled.show()
    time.sleep(0.75)
    oled.text("now start. The", 0, 10)
    oled.show()
    time.sleep(0.75)
    oled.text("LED should light", 0, 20)
    oled.show()
    time.sleep(0.75)
    oled.text("up now. Have fun", 0, 30)
    oled.show()
    time.sleep(2)
    # END

    # Turns the LED on
    LED.value(1)

    # Clears the OLED screen
    oled.fill(0)
    oled.show()

    # Wait between 5~10 secs before turning off the LED
    time.sleep(randint(5,10))
    
    # Turns off the LED and starts the timer
    LED.value(0)
    startTime = time.ticks_ms()

    # Wait for the button to be released if it was pressed before the LED turned off
    anti_cheating_single()

    # Now wait for the button press after the LED turns off
    while True:
        if BTN_L.value() == 1:
            pressTime = time.ticks_ms()
            reactionTime = time.ticks_diff(pressTime, startTime)
            break
        time.sleep(0.001)

    # Clears the screen and prints the message
    oled.fill(0)
    oled.text("Your reaction", 0, 0)
    oled.text(f"time was {reactionTime} ms", 0, 10)
    oled.show()




    
def duo_game_loop():
    pass

def main():
    LED.value(0)
    select_mode()

if __name__ == "__main__":
    #test()
    main()
