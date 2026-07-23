import math
import pyautogui

class MouseController:

    def __init__(self):

        self.screen_width, self.screen_height = pyautogui.size()

        pyautogui.FAILSAFE = False

        self.dragging = False

    def move(self, x, y):
        pyautogui.moveTo(x, y)

    def left_click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def drag_start(self):

        if not self.dragging:
            pyautogui.mouseDown()
            self.dragging = True

    def drag_stop(self):

        if self.dragging:
            pyautogui.mouseUp()
            self.dragging = False

    def scroll(self, amount):
        pyautogui.scroll(amount)

    def distance(self, p1, p2, width, height):

        x1 = int(p1.x * width)
        y1 = int(p1.y * height)

        x2 = int(p2.x * width)
        y2 = int(p2.y * height)

        return math.hypot(x2 - x1, y2 - y1)

    def scroll(self, amount):
    pyautogui.scroll(amount) 