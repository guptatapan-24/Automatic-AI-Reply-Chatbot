# AutoResponder Script

## Description
The AutoResponder Script is a Python-based automation tool that responds to chat messages using Google Generative AI. It captures chat history and generates context-aware replies based on the last message from a specified sender. This script is useful for automating responses in messaging applications.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [Configuration](#configuration)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)
- [Acknowledgments](#acknowledgments)

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Required Python packages:
  - `pyautogui`
  - `pyperclip`
  - `keyboard`
  - `google-generativeai`

## Installation Instructions
You can install the required packages using pip:

```bash
pip install pyautogui pyperclip keyboard google-generativeai

## Usage Instructions
1. **Run the Script:**
   Execute the script in your terminal:

   ```bash
   python auto_responder.py
2. **Hotkey:**
   Press the q key at any time to stop the script.

3. **Functionality:**
The script waits for a chat message from a specific sender.
It captures the chat history upon detecting the message.
It generates a response using Google Generative AI and sends it back to the chat.

## Configuration
1. **API Key:**
   Ensure you have a valid API key for Google Generative AI. Set it as an environment variable named API_KEY.

2. **Coordinates Configuration:**
   The script uses hardcoded screen coordinates for mouse actions. Adjust these coordinates to match your screen resolution and the application you are automating.

## Features
1. Automatically responds to chat messages based on the sender.
2. Context-aware replies generated using Google Generative AI.
3. User-friendly interface with a stop command via a hotkey.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact Information
For support or inquiries, please contact:

Name: Tapan Gupta
Email: gupta.tapan2006@gmail.com

## Acknowledgments
Google Generative AI for providing the AI capabilities.
PyAutoGUI for GUI automation.
Pyperclip for clipboard management.
Keyboard for handling hotkeys.
