import time
import os
import board
import digitalio

print("press a button!")

button1 = digitalio.DigitalInOut(board.D23)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D24)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.D25)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.D17)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

button5 = digitalio.DigitalInOut(board.D22)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

while True:

    # omxplayer -o local <file>
    # omxplayer -o hdmi <file>
    # omxplayer -o both <file>
    if not button1.value:
        os.system('omxplayer L.mp3 &')

    if not button2.value:
        os.system('omxplayer L2.mp3 &')

    if not button3.value:
        os.system('omxplayer L3.mp3 &')
        
    if not button4.value:
        os.system('omxplayer L4.mp3 &')

    if not button5.value:
        os.system('omxplayer L5.mp3 &')

    time.sleep(.15)
