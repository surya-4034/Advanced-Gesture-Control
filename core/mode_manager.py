class ModeManager:

    def __init__(self):
        self.mode = "MOUSE"

    def current(self):
        return self.mode

    def next_mode(self):

        modes = [
            "MOUSE",
            "PRESENTATION",
            "DRAW",
            "MEDIA"
        ]

        index = modes.index(self.mode)

        self.mode = modes[(index + 1) % len(modes)]

    def set_mode(self, mode):

        self.mode = mode