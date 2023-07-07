
import pyautogui
import time

# Press the Windows key to open the Start menu.
pyautogui.press('win')

# Type the name of the application you want to open.
pyautogui.write('google chrome')

# Press the Enter key to open the application.
pyautogui.press('enter')

# Wait for the application to open.
time.sleep(2)

# Type the search term in the address bar.
pyautogui.write('ai')

# Press the Enter key to submit the search.
pyautogui.press('enter')
