import pyautogui
import pyperclip
import time
import os
from google import generativeai as genai

# Give a short delay before the script runs
time.sleep(2)

def is_last_message_from_sender(chat_log, sender_name):
    messages=chat_log.strip().split("/2024]")[-1]
    if sender_name in messages:
        return True
    return False
   

# Step 1: Click on the icon at coordinates (515, 894)
pyautogui.click(512, 18)
time.sleep(1)

while True:
    # Step 2: Drag from (681, 211) to (685, 962) to select the text
    pyautogui.moveTo(682, 210)
    pyautogui.dragTo(695, 965, duration=1, button='left')

    # Step 3: Copy the selected text (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1855, 439)
    time.sleep(1)

    # Step 4: Get the copied text from the clipboard
    chat_history = pyperclip.paste()

    # Store the copied text into a variable and print it
    print(chat_history)

    if is_last_message_from_sender(chat_history, "Siddhesh"):
        def gemini(command):
            # Access API key from environment variable
            api_key = os.getenv('API_KEY')

            # Use the api_key in your code
            genai.configure(api_key=api_key)

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
