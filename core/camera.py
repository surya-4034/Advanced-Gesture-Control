import cv2


class Camera:

    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            raise Exception("Unable to open webcam.")

    def read(self):
        success, frame = self.cap.read()
        return success, frame

    def release(self):
        self.cap.release()

    @staticmethod
    def show(window_name, frame):
        cv2.imshow(window_name, frame)

    @staticmethod
    def close():
        cv2.destroyAllWindows()