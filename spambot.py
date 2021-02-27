from pynput.keyboard import Key, Controller 
import keyboard
import time

message = "Message Here"
keyboard = Controller()

def banner():
	print("                                    _ \n")
	print("  ___ _ __   __ _ _ __ ___   __   _/ |\n")
	print(" / __| '_ \ / _` | '_ ` _ \  \ \ / / |\n")
	print(" \__ \ |_) | (_| | | | | | |  \ V /| |\n")
	print(" |___/ .__/ \__,_|_| |_| |_|   \_/ |_|\n")
	print("     |_|                              \n")
banner()

print(f"Make sure your mouse hovers and clicks on an input field for script to work")
print(f"starting in 10 sec")

time.sleep(10)
for num in range(100):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    