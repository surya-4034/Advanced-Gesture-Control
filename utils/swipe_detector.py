class SwipeDetector:

    def __init__(self):

        self.last_x = None
        self.threshold = 120

    def detect(self, x):

        if self.last_x is None:
            self.last_x = x
            return None

        diff = x - self.last_x

        self.last_x = x

        if diff > self.threshold:
            return "RIGHT"

        elif diff < -self.threshold:
            return "LEFT"

        return None