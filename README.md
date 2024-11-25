# Reaction Game
By QinCai, https://qincai.xyz

## Description
This is a simple (but not so simple) hardware game, where one or two players press a button after a LED turns off. The reaction time is the time between the LED turns off and the user presses the button. The program will also provide feedback on your reaction time. 

## How to Play
There are two ways you could use the program. You can either build it physically or just simulate it.

### Simulate it!
1. Head your browser to https://wokwi.com/projects/406241938731148289 and press the green circle with a triangle inside! The game might be slow, and the timer might not work properly, depending on the device you are using.

2. Read and follow the instructions displayed on the OLED screen.

3. Press your button (or 1 on the keyboard for the Left button, 2 for the Right button) as soon as the LED turns off. No cheating by pressing and holding the button! The program won't allow you to do that muahahaha! ; )

4. Your reaction time will be displayed on the OLED screen. If you are in two-player mode, only the reaction time of the fastest person that presses will be displayed!

#### Screenshots
![Screenshot 2024-08-22 12 15 21](https://github.com/user-attachments/assets/c765972f-fe54-4b15-8c93-0bdea4259904)
![image](https://github.com/user-attachments/assets/e88b1e7c-d5e7-41f9-94d4-9fd805ee358a)
![image](https://github.com/user-attachments/assets/e91a72f8-a2cf-4d06-a52e-9656da1a99cb)
![image](https://github.com/user-attachments/assets/80b78707-d790-49d0-aa5c-48d67ddb4585)

#### Features
1. Wokwi simulation right in your browser (for free!)
2. OLED screen for displaying instructions
3. An on-board LED
4. Two buttons
5. Powered by a Raspberry Pi Pico

#### Requirements
1. A modern browser
2. A considerably fast computer of some kind

#### Installation
1. A modern browser if you don't have one (which is highly unlikely because you are reading this...)
2. Just head type https://wokwi.com/projects/406241938731148289 into your browser and press the green circle with a triangle in it to start playing!


### Build it physically!
It is quite easy to actually build it. Refer to https://wokwi.com/projects/406241938731148289 for the diagram. 

#### Requirements
1. Raspberry Pi Pico/W/WH; probably will work on a Pico 2, although not tested. 
2. Half breadboard or larger
3. SSD1306 128x64 OLED display
4. Two momentary-on pushbuttons
5. 4 to 8 male-to-male jumper wires, depending on the type of buttons you are using.
6. A micro-USB data cable
7. A computer with VS Code or Thonny or other IDE with the ability to interface with the RPi Pico

#### How to use it
1. Run `git clone https://github.com/QinCai-rui/Reaction-Game.git` inside a Terminal on your computer
2. Install an IDE compatible with the RPi Pico if you haven't done so (I recommend Thonny to beginners)
3. Build the circuit
4. Connect the Pico to your computer using a microUSB cable
5. Open up the `main.py` and `ssd1306.py` in Thonny and save it into your Pi Pico
6. Run the code and enjoy!! :))
