
# WhatsApp Web Auto Reply Bot 🤖

This is a Python-based WhatsApp Web auto-reply bot that reads chat history from WhatsApp Web, processes the conversation using Google Gemini AI, and replies automatically as "Jayshree" with a personalized AI response.


## Features

- Automatically reads WhatsApp Web chat messages using **PyAutoGUI** and **Pyperclip**.
- Sends chat history to Google Gemini AI to generate context-aware replies.
- Replies only if the last message is from the other person (prevents self-replies).
- Pastes AI-generated replies directly into WhatsApp Web chat using GUI automation.
- Mimics a persona named "Jayshree" (an Indian woman coder) for more natural conversations.
- Fully automated interaction without manual typing.


## Requirements

- Python 3.x
- Modules:
  - `pyautogui`
  - `pyperclip`
  - `google-genai` (for Google Gemini API integration)
  - `time` (standard library)

## Installation

Install required Python packages:

```bash
pip install pyautogui pyperclip google-genai

```
    
## Note

- For pyautogui, you may need additional dependencies depending on your OS.
- This script automates mouse clicks, so ensure your screen resolution and WhatsApp Web layout match the coordinates used (or update them accordingly). [use file "cursor_position.py" to identify the coordinates]

## Setup

1. Get Google Gemini API key:
    Obtain your API key and update the script's variable:

```python
gemini_api_key = "YOUR_GEMINI_API_KEY"

```
2. Open WhatsApp Web in Chrome and make sure chats are visible.

3. Adjust screen coordinates in the script if necessary:

- Clicking Chrome icon
- Selecting WhatsApp chat
- Copying chat history
- Pasting reply
- send button


## Usage/Examples

Run the script:

```bash
python main.py
```

The bot will continuously monitor the WhatsApp Web chat:
- It reads the latest messages by selecting and copying chat text.
- Sends chat history to the AI to generate a reply.
- Pastes the reply if the last message was from the other person.
- Skips replying if the last message was sent by "Jayshree".


## Important Notes
- The bot uses screen coordinates for mouse clicks and drags. If your WhatsApp Web layout or screen resolution changes, update the coordinates accordingly in the script.
- The script depends on clipboard access for copying and pasting.
- Requires an active internet connection for AI response generation.
- Designed for personal use and learning purposes. Use responsibly.
- The bot currently assumes a fixed persona named "Jayshree" for AI response context.

## How It Works (Brief)
- Clicks Chrome and opens WhatsApp Web.
- Selects chat area, drags mouse to highlight messages.
- Copies the selected chat history to clipboard.
- Checks if the last message sender is not "Jayshree".
- Sends chat history to Google Gemini API with instructions to behave like "Jayshree".
- Gets AI-generated reply, copies to clipboard.
- Pastes the reply in the chat input box and sends.

## Troubleshooting & Customization
- Adjust the pyautogui.click(x, y) and dragTo coordinates to match your screen and WhatsApp Web layout.
- Add logging or print statements for debugging.
- Customize AI prompt messages to change the personality or style of replies.
- Integrate error handling for clipboard or API failures.


## License

This project is open source and free to use for personal and educational purposes.



## Authors

[@i-JayshreeChauhan](https://github.com/i-JayshreeChauhan)

