import pyautogui    
import time
import pyperclip
import re
from openai import OpenAI
from config import get_settings

api_key, model = get_settings()
client = OpenAI(api_key=api_key)



        # Small delay to give you time to switch to the correct window
time.sleep(1)

pyautogui.click(977, 1052)
            # Step 1: Click on the icon

            # Small delay after click
time.sleep(1)

while True:
        # Step 2: Drag to select text
    pyautogui.click(593, 134)
    pyautogui.keyDown('shift')
    pyautogui.click(1882,915, duration=1 )  # smooth drag
    pyautogui.keyUp('shift')

            # Step 3: Copy to clipboard
    pyautogui.hotkey('ctrl', 'c') 
    pyautogui.click(1231,834) 
           # Small delay after selection
    time.sleep(1)


    chat_history = pyperclip.paste() or ""

    print(chat_history) 
        
    completion = client.chat.completions.create(
            model=model,
            messages=[
                    {"role": "system", "content": "you are paras. reply in natural hinglish. output only the message text. do not include date, time, sender name, prefixes, labels, or chat format."},
                        {"role": "user", "content": chat_history}
                    ]
                )
            

    response = completion.choices[0].message.content or ""
        

    pyperclip.copy(response)

    pyautogui.click(1150,973)
    time.sleep(1)

    pyautogui.hotkey('ctrl','v')
    time.sleep(1) 


pyautogui.press('enter')
        
if __name__ == "__main__":
    is_last_message_from_sender("")
