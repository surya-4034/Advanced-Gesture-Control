import cv2
import mediapipe as mp


class HandTracker:

    def __init__(self):
        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        print(results.multi_hand_landmarks)

        return results

    def draw(self, frame, results):
        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

                self.drawer.draw_landmarks(
                    frame,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )

    def get_landmarks(self, results):
        if not results.multi_hand_landmarks:
            return None

        hand = results.multi_hand_landmarks[0]

        return hand.landmark