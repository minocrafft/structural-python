import cv2
from pydantic import PositiveInt, PositiveFloat


class OpencvStream:
    """
    The object of opencv stream for using cv2.VideoCapture objects.
    This object is made in the 'Proxy' pattern.
    """

    def __init__(self, src: str):
        self.src: str = src
        self.cap: cv2.VideoCapture = cv2.VideoCapture(src)
        self.count: PositiveInt = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.width: PositiveInt = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height: PositiveInt = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps: PositiveFloat = self.cap.get(cv2.CAP_PROP_FPS)

    @property
    def pos_frame(self):
        return self.cap.get(cv2.CAP_PROP_POS_FRAMES)

    def read(self):
        return self.cap.read()

    def set(self, *args, **kwargs):
        self.cap.set(*args, **kwargs)

    def release(self):
        self.cap.release()
