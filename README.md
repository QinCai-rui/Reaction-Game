# Reaction Game
By QinCai, https://qincai.xyz

## Description
This is a simple (but not so simple) hardware game, where one or two players press a button after a LED turns off. The reaction time is the time between the LED turns off and the user presses the button. The program will also provide feedback on your reaction time. 

## Build it physically!
It is quite easy to actually build it. Refer to https://wokwi.com/projects/406241938731148289 for the diagram. 

### Requirements
1. Raspberry Pi Pico/W/WH; probably will work on a Pico 2, although not tested. 
2. Half breadboard or larger
3. SSD1306 128x64 OLED display
4. Two momentary-on pushbuttons
5. 4 to 8 male-to-male jumper wires, depending on the type of buttons you are using.
6. A micro-USB data cable
7. A computer with VS Code or Thonny or other IDE with the ability to interface with the RPi Pico

### How to use it
1. Run `git clone https://github.com/QinCai-rui/Reaction-Game.git` inside a Terminal on your computer
2. Install an IDE compatible with the RPi Pico if you haven't done so (I recommend Thonny to beginners)
3. Build the circuit
4. Connect the Pico to your computer using a microUSB cable
5. Open up the `main.py` and `ssd1306.py` in Thonny and save it into your Pi Pico
6. Run the code and enjoy!! :))
