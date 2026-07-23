import math


class GestureEngine:

    def __init__(self):

        self.click_threshold = 30
        self.right_click_threshold = 30
        self.drag_threshold = 25

    def distance(self, p1, p2, width, height):

        x1 = int(p1.x * width)
        y1 = int(p1.y * height)

        x2 = int(p2.x * width)
        y2 = int(p2.y * height)

        return math.hypot(x2 - x1, y2 - y1)

    def finger_states(self, landmarks):

        fingers = []

        # Thumb
        fingers.append(landmarks[4].x > landmarks[3].x)

        # Index
        fingers.append(landmarks[8].y < landmarks[6].y)

        # Middle
        fingers.append(landmarks[12].y < landmarks[10].y)

        # Ring
        fingers.append(landmarks[16].y < landmarks[14].y)

        # Pinky
        fingers.append(landmarks[20].y < landmarks[18].y)

        return fingers

    def detect(self, landmarks, w, h):

        thumb = landmarks[4]
        index = landmarks[8]
        middle = landmarks[12]
        ring = landmarks[16]

        thumb_index = self.distance(thumb, index, w, h)
        thumb_middle = self.distance(thumb, middle, w, h)
        thumb_ring = self.distance(thumb, ring, w, h)

        fingers = self.finger_states(landmarks)

        # Pinch Gestures
        if thumb_index < self.click_threshold:
            return "LEFT_CLICK"

        if thumb_middle < self.right_click_threshold:
            return "RIGHT_CLICK"

        if thumb_ring < self.drag_threshold:
            return "DRAG"

        # Finger-state gestures
        # Open Palm
        if fingers == [True, True, True, True, True]:
            return "NEXT_SLIDE"

        # Three Fingers
        if fingers == [False, True, True, True, False]:
            return "PREVIOUS_SLIDE"

        # Index Finger Only
        if fingers == [False, True, False, False, False]:
            return "MOVE"

        # Index + Middle finger open
        if fingers == [False, True, True, False, False]:
            return "SCROLL"
        return "MOVE"