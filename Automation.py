import pyautogui
import subprocess

pyautogui.moveTo(10,10, duration=1)
pyautogui.moveTo(100,400, duration=2)
pyautogui.moveTo(400,400, duration=1)

pyautogui.leftClick(500,500)
pyautogui.rightClick(300,400)

subprocess.Popen(["C:\windows\system32\\notepad.exe"])


pyautogui.sleep(1)
pyautogui.hotkey('win','up')
