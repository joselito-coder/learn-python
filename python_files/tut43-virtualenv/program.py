# this program copies harry bhai is the best to the clipboard and then pastes it 3 times
import pyperclip
import pyautogui

# copies to clipboard
pyperclip.copy("harry bhai is the best\n")

# pastes the text "harry bhai is the best" 3 times
for i in range(3):
    pyautogui.hotkey('ctrl','v')
