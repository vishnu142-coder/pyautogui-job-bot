import pyautogui
import time
import pyperclip

print("Starting in 5 seconds...")
time.sleep(5)

pyautogui.hotkey('command', 'space')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(5)

pyperclip.copy('https://www.google.com')
pyautogui.hotkey('command', 'l')
pyautogui.hotkey('command', 'v')
pyautogui.press('enter')

time.sleep(3)

# Search for jobs
pyperclip.copy('Software Engineer jobs for freshers')
pyautogui.write(pyperclip.paste())
pyautogui.press('enter')

time.sleep(5)

print("Task Completed ✅")
