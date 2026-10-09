import os
import pyautogui


def take_screenshot():

    image = pyautogui.screenshot()

    image.save("screenshot.png")

    return "Screenshot has been saved."


def shutdown_system():

    os.system("shutdown /s /t 5")

    return "Shutting down the computer in 5 seconds."


def restart_system():

    os.system("shutdown /r /t 5")

    return "Restarting the computer in 5 seconds."


def lock_system():

    os.system("rundll32.exe user32.dll,LockWorkStation")

    return "Locking the computer."