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
import ssd1306
import time

# Initialise the LED
LED = Pin(26, Pin.OUT)

# Initialise the buttons
BTN_RED = Pin(19, Pin.IN, Pin.PULL_DOWN)
BTN_GREEN = Pin(18, Pin.IN, Pin.PULL_DOWN)

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
    if BTN_RED.value() == 1: 
        LED.value(1)
        time.sleep(1)
    LED.value(0)

def select_player_mode():
    oled.fill(0)
    oled.text("Select Player Mode", 0, 0)
    oled.show()
    time.sleep(0.75)
    oled.text("Press the left button for 1 player", 0, 0)
    oled.show()

LED.value(1)

test()
select_player_mode()
