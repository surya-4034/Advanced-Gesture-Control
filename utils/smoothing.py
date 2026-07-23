class SmoothCursor:

    def __init__(self, smoothening=7):
        self.smoothening = smoothening

        self.prev_x = 0
        self.prev_y = 0

    def smooth(self, x, y):

        current_x = self.prev_x + (x - self.prev_x) / self.smoothening
        current_y = self.prev_y + (y - self.prev_y) / self.smoothening

        self.prev_x = current_x
        self.prev_y = current_y

        return current_x, current_y