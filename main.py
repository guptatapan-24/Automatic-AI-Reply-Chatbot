import pyautogui
import pyperclip
import time

while True:
    a=pyautogui.position()
    print(a)


# Give a short delay before the script runs
time.sleep(2)

# Step 1: Click on the icon at coordinates (515, 894)
pyautogui.click(515, 894)

# Step 2: Drag from (681, 211) to (685, 962) to select the text
pyautogui.moveTo(681, 211)
pyautogui.dragTo(685, 962, duration=1, button='left')

# Step 3: Copy the selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')

# Step 4: Get the copied text from the clipboard
copied_text = pyperclip.paste()

# Store the copied text into a variable and print it
print(f"Copied Text: {copied_text}")

    # 515 894
    # 681 211
    # 685 962