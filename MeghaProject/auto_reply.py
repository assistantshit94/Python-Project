
import pyautogui
import pyperclip
import time
import os
from openai import OpenAI

# --------------------------------
# 1. Initialize OpenAI
# --------------------------------


import os
from dotenv import load_dotenv
from openai import OpenAI

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)
# Safety: move mouse to top-left corner to abort PyAutoGUI
pyautogui.FAILSAFE = True


# --------------------------------
# 2. Select and copy the message
# --------------------------------

print("Starting message selection...")

# Click the icon
pyautogui.click(1795, 376)
time.sleep(1)

# Select the message
pyautogui.moveTo(706, 224, duration=0.5)
pyautogui.dragTo(960, 910, duration=1)

time.sleep(0.5)

# Copy selected text
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

# Store copied text
copied_text = pyperclip.paste()

if not copied_text.strip():
    print("No text selected. Please check your coordinates.")
    raise SystemExit

print("\nOriginal message:")
print(copied_text)


# --------------------------------
# 3. Generate reply using OpenAI
# --------------------------------

print("\nGenerating reply...")

try:
    response = client.responses.create(
        model="gpt-5.5",
        instructions=(
            "You are a helpful message reply assistant. "
            "Read the received message and write a natural, "
            "polite and relevant reply. Keep it concise and human. "
            "Do not invent personal facts or commitments. "
            "Return only the reply message."
        ),
        input=copied_text
    )

    generated_reply = response.output_text.strip()

except Exception as e:
    print("OpenAI API error:", e)
    raise SystemExit


if not generated_reply:
    print("OpenAI returned an empty reply.")
    raise SystemExit


# --------------------------------
# 4. Display generated reply
# --------------------------------

print("\nGenerated reply:")
print("--------------------------------")
print(generated_reply)
print("--------------------------------")

# Copy reply to clipboard
pyperclip.copy(generated_reply)


# --------------------------------
# 5. Confirm before sending
# --------------------------------

choice = input("\nDo you want to send this reply? (y/n): ")

if choice.lower().strip() == "y":

    print("\nYou have 5 seconds.")
    print("Switch to your messaging app and click its reply box.")

    for i in range(5, 0, -1):
        print("Sending in", i)
        time.sleep(1)

    # Paste generated reply
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    # Send message
    pyautogui.press("enter")

    print("\nReply sent!")

else:
    print("\nSending cancelled.")
    print("Generated reply is still available in your clipboard.")
