import pyautogui
import time
import pyperclip
from google import genai

gemini_api_key = "<api_key>"


def ai_reply_process(chathistory):
    client = genai.Client(api_key=gemini_api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=chathistory + " (refer this chat history - you are the person named as Jayshree , you are an indian women and a coder by profession - behave like her and respond (dont built or generate msg for others) )",
    )

    reply_msg = response.text.replace("*"," ") #replacing all * with spaces
    print("\n")
    print(reply_msg)


    index = reply_msg.find("ee:")
    if(index!=-1):
        sliced_reply_msg = reply_msg[(index+3):]
    else:
        sliced_reply_msg = reply_msg


    # index=0
    # index = reply_msg.find("2025]")
    # if(index!=-1):
    #     sliced_reply_msg = sliced_reply_msg[(index+5):]
    # else:
    #     sliced_reply_msg = sliced_reply_msg

    pyperclip.copy(sliced_reply_msg)
    pyautogui.click(629,688)
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.click(1326,688)
    time.sleep(1)




# --- Check if the last message is by the sender (not Jayshree) ---
def is_last_msg_from_sender(chat_text):
    # Split into lines and go backwards to find the last non-empty message
    lines = chat_text.strip().split('\n')

    for line in reversed(lines):
        if line.strip():
            # Check if Jayshree sent it
            if "Jayshree" in line:
                return False
            else:
                return True
    return False




#---------------- Actual Program starting from here

#click on chrome icom
pyautogui.click(948,745)
time.sleep(1)  #wait till 1 sec , to ensure it get registered

while True:
    #click on whatsapp chat 
    pyautogui.moveTo(491,160)
    time.sleep(1)
    pyautogui.click(491,160)
    time.sleep(1)  #wait till 1 sec to make sure click is registered

    #drag from one position to other to copy data
    pyautogui.dragTo(1333,643 , duration=2.0 , button='left')  #drag for 1 sec 

    #copy the selected item
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)  #wait till 1 sec to make sure copying is done
    pyautogui.click(1328,188)  #this click is to deselct the selected stuff

    #retrieve the text from the clipboard and store it in a variable
    chathistory = pyperclip.paste()

    while(chathistory == ""):  #empty
        #click on chrome icom
        pyautogui.click(948,745)
        time.sleep(1)  #wait till 1 sec , to ensure it get registered

        #click on whatsapp chat 
        pyautogui.moveTo(571,156)
        time.sleep(1)
        pyautogui.click(571,156)
        time.sleep(1)  #wait till 1 sec to make sure click is registered

        #drag from one position to other to copy data
        pyautogui.dragTo(1087,648 , duration=2.0 , button='left')  #drag for 1 sec 

        #copy the selected item
        pyautogui.hotkey('ctrl','c')
        time.sleep(1)  #wait till 1 sec to make sure copying is done
        pyautogui.click(1328,188)  #this click is to deselct the selected stuff

        #retrieve the text from the clipboard and store it in a variable
        chathistory = pyperclip.paste()

    print(chathistory)
    #ai_reply_process(chathistory)

    # Only process if last message is from someone else
    if is_last_msg_from_sender(chathistory):
        ai_reply_process(chathistory)
    else:
        print("Last message is from Jayshree. No response generated.")




