import pyautogui
import pyperclip
import time
import os
import keyboard
from google import generativeai as genai

# Give a short delay before the script runs
time.sleep(2)

def is_last_message_from_sender(chat_log, sender_name):
    messages=chat_log.strip().split("/2024]")[-1]
    if sender_name in messages:
        return True
    return False
   
running = True

def stop_script():
    global running
    running=False

keyboard.add_hotkey("q", stop_script)
# Step 1: Click on the icon at coordinates (515, 894)
pyautogui.click(512, 18)
time.sleep(1)

while running:

    # Step 2: Clicks on the name of the sender
    pyautogui.click(814, 164)
    time.sleep(1)

    # Step 3: Selects and copies a part of the name of the sender
    pyautogui.moveTo(1537, 528)
    pyautogui.dragTo(1693, 527, duration=1, button="left")
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(1855, 439)
    time.sleep(1)

    # Step 4: Gets the copied sender name from the clipboard
    pyautogui.click(1382, 169)
    time.sleep(1)

    # Stores the copied username in a variable
    user_name_part=pyperclip.paste()

    # Step 5: Drag from (681, 211) to (685, 962) to select the text
    pyautogui.moveTo(682, 210)
    pyautogui.dragTo(1266, 888, duration=1, button='left')

    # Step 6: Copy the selected text (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1855, 439)
    time.sleep(1)

    # Step 7: Get the copied text from the clipboard
    chat_history = pyperclip.paste()

    # Store the copied text into a variable and print it
    print(chat_history)

    if is_last_message_from_sender(chat_history, user_name_part):
        def gemini(command):
            my_key=os.getenv("API_KEY")
            genai.configure(api_key=my_key)

            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"You are a person named Tapan, who speaks Hindi as well as English. You are from India, study in RVCE Bengaluru and are a coder. You have to analyze the chat history and respond like Tapan. Respond after properly analyzing the chat. Output should be the next chat response. Don't include the message time and date in your response. Reply in english if the sender types in english, else in Hindi. {command}")
            return response.text

        command = chat_history

        reply=gemini(command)

        print(reply)

        pyautogui.click(845, 958)
        time.sleep(1)

        pyperclip.copy(reply)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')