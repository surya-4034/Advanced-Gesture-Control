import cv2

from core.camera import Camera
from core.hand_tracker import HandTracker
from core.gesture_engine import GestureEngine
from core.mode_manager import ModeManager

from controllers.mouse_controller import MouseController
from controllers.presentation_controller import PresentationController

from utils.smoothing import SmoothCursor


# -----------------------------
# Initialize
# -----------------------------

camera = Camera()
tracker = HandTracker()
gesture = GestureEngine()

mouse = MouseController()
presentation = PresentationController()

smoother = SmoothCursor()
mode = ModeManager()

margin = 120
clicking = False


# -----------------------------
# Main Loop
# -----------------------------

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
        # Active Mouse Area
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

        if mode.current() == "MOUSE":
            mouse.move(screen_x, screen_y)

        cv2.circle(
            frame,
            (x, y),
            12,
            (0, 255, 0),
            -1,
        )

        # -----------------------------
        # Gesture Detection
        # -----------------------------

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

        # -----------------------------
        # Mouse Mode
        # -----------------------------

        if mode.current() == "MOUSE":

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

            else:

                mouse.drag_stop()
                clicking = False

        # -----------------------------
        # Presentation Mode
        # -----------------------------

        elif mode.current() == "PRESENTATION":

            if current_gesture == "NEXT_SLIDE":

                presentation.next_slide()

            elif current_gesture == "PREVIOUS_SLIDE":

                presentation.previous_slide()

    else:
        clicking = False
        mouse.drag_stop()

    # -----------------------------
    # UI
    # -----------------------------

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
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
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