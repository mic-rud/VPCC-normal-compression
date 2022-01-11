import cv2
import numpy as np

class VideoCapture:
    def __init__(self, filename, size, convert=True):
        self.width, self.height = size
        self.frame_len = int(self.width * self.height * 3 / 2)
        self.shape = (int(self.height*1.5), self.width)
        self.convert = convert

        self.f = self.read_file(filename)



    def read_file(self, filename):
        try:
            file = open(filename, 'rb')
        except Exception as e:
            print(str(e))
            return None
        return file



    def read_raw(self):
        try:
            raw = self.f.read(self.frame_len)
            yuv = np.frombuffer(raw, dtype=np.uint8)
            if len(yuv) != 0:
                yuv = yuv.reshape(self.shape)
            else:
                return False, None
        except Exception as e:
            print(str(e))
            return False, None
        return True, yuv

    def read(self):
        ret, yuv = self.read_raw()
        if not ret:
            return ret, yuv
        if self.convert:
            bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
        else:
            bgr = yuv
        return ret, bgr
