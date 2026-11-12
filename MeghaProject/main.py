# import pyautogui

# while True:

#     a = pyautogui.position()
#     print(a)
#     1795 376
    
#     706 224 to 960 910

import pyautogui
import pyperclip
import time

# Step 1: Click on the icon
pyautogui.click(1795, 376)
time.sleep(1)

# Step 2: Select text by dragging
pyautogui.moveTo(706, 224, duration=0.5)
pyautogui.dragTo(960, 910, duration=1)

time.sleep(0.5)

# Step 3: Copy selected text
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

# Step 4: Get copied text into a variable
copied_text = pyperclip.paste()

# Step 5: Print copied text
print("Copied Text:")
print(copied_text)