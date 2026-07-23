import pyautogui


class PresentationController:

    def __init__(self):
        pyautogui.FAILSAFE = False

    def next_slide(self):
        pyautogui.press("right")

    def previous_slide(self):
        pyautogui.press("left")

    def start_slideshow(self):
        pyautogui.press("f5")

    def exit_slideshow(self):
        pyautogui.press("esc")