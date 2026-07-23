import cv2

from core.camera import Camera
from core.hand_tracker import HandTracker
from core.gesture_engine import GestureEngine
from core.mode_manager import ModeManager

from controllers.mouse_controller import MouseController
from controllers.presentation_controller import PresentationController

from utils.smoothing import SmoothCursor
from utils.swipe_detector import SwipeDetector


camera = Camera()
tracker = HandTracker()
gesture = GestureEngine()

mouse = MouseController()
presentation = PresentationController()

smoother = SmoothCursor()
mode = ModeManager()
swipe = SwipeDetector()

margin = 120
clicking = False

while True:

    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    results = tracker.process(frame)

    tracker.draw(frame, results)

    landmarks = tracker.get_landmarks(results)

    if landmarks:

        h, w, _ = frame.shape

        index = landmarks[8]

        x = int(index.x * w)
        y = int(index.y * h)

        # -----------------------------
        # Active Area
        # -----------------------------

        cv2.rectangle(
            frame,
            (margin, margin),
            (w - margin, h - margin),
            (255, 0, 255),
            2,
        )

        x = max(margin, min(x, w - margin))
        y = max(margin, min(y, h - margin))

        screen_x = (x - margin) * mouse.screen_width / (w - 2 * margin)
        screen_y = (y - margin) * mouse.screen_height / (h - 2 * margin)

        screen_x, screen_y = smoother.smooth(
            screen_x,
            screen_y,
        )

        cv2.circle(
            frame,
            (x, y),
            12,
            (0, 255, 0),
            -1,
        )

        current_gesture = gesture.detect(
            landmarks,
            w,
            h,
        )

        cv2.putText(
            frame,
            f"Gesture : {current_gesture}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2,
        )

        # ====================================
        # MOUSE MODE
        # ====================================

        if mode.current() == "MOUSE":

            mouse.move(screen_x, screen_y)

            if current_gesture == "LEFT_CLICK":

                if not clicking:
                    mouse.left_click()
                    clicking = True

            elif current_gesture == "RIGHT_CLICK":

                if not clicking:
                    mouse.right_click()
                    clicking = True

            elif current_gesture == "DRAG":

                mouse.drag_start()
                clicking = False
            
            elif current_gesture == "SCROLL":

    middle = landmarks[12]

    if middle.y < 0.45:

        mouse.scroll(80)

        cv2.putText(
            frame,
            "SCROLL UP",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2,
        )

    elif middle.y > 0.60:

        mouse.scroll(-80)

        cv2.putText(
            frame,
            "SCROLL DOWN",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2,
        )

            clicking = False
            else:

                mouse.drag_stop()
                clicking = False

        # ====================================
        # PRESENTATION MODE
        # ====================================

        elif mode.current() == "PRESENTATION":

            swipe_direction = swipe.detect(x)

            if swipe_direction == "RIGHT":

                presentation.next_slide()

                cv2.putText(
                    frame,
                    "NEXT SLIDE ➜",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2,
                )

            elif swipe_direction == "LEFT":

                presentation.previous_slide()

                cv2.putText(
                    frame,
                    "⬅ PREVIOUS SLIDE",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2,
                )

    else:

        clicking = False
        mouse.drag_stop()

    # ====================================
    # UI
    # ====================================

    cv2.putText(
        frame,
        "GesturePilot AI",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.putText(
        frame,
        f"Mode : {mode.current()}",
        (20, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2,
    )

    cv2.putText(
        frame,
        "Press M : Change Mode",
        (20, 200),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2,
    )

    camera.show(
        "GesturePilot AI",
        frame,
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("m"):
        mode.next_mode()

    elif key == ord("q"):
        break

camera.release()
camera.close()