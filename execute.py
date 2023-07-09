import pyautogui
import webbrowser

# Press the Windows key to open the Start menu.
pyautogui.press('win')

# Type "google chrome" and press Enter.
pyautogui.write('google chrome')
pyautogui.press('enter')

# Wait for Google Chrome to open.
webbrowser.get('chrome').open('https://www.google.com/search?q=ai')
