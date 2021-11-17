import cv2
import numpy as np

class VideoCaptureYUV:
    def __init__(self, filename, size):
        self.height, self.width = size
        self.frame_len = int(self.width * self.height * 3 / 2)
        print(self.frame_len)
        self.f = open(filename, 'rb')
        self.shape = (int(self.height*1.5), self.width)

    def read_raw(self):
        try:
            raw = self.f.read(self.frame_len)
            yuv = np.frombuffer(raw, dtype=np.uint8)
            yuv = yuv.reshape(self.shape)
        except Exception as e:
            print(str(e))
            return False, None
        return True, yuv

    def read(self):
        ret, yuv = self.read_raw()
        if not ret:
            return ret, yuv
        bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
        return ret, bgr


if __name__ == "__main__":
    maps = ["attribute", "geometry", "occupancy"]
    sizes = {
        "attribute" : (1664, 1280),
        "geometry" : (1664, 1280),
        "occupancy" : (416, 320)
    }
    for map in maps:
        i = -1
        size = sizes[map]
        out = cv2.VideoWriter('results/' + map + '.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 5, (size[1], size[0]))
        for GOF in [2]:
            size_string = str(size[1]) + 'x' + str(size[0])
            filename = "S26C03R03_GOF" + str(GOF) + "_" + map + "_" + size_string + "_8bit_p420.yuv"
            print(filename)
            cap = VideoCaptureYUV(filename, size)

            while 1:
                ret, frame = cap.read()
                if ret:
                    i = i+1
                    print(frame.shape)

                    if map == 'geometry':
                        f0 = frame[:,:,0] #Not used
                        f1 = frame[:,:,1]
                        f2 = frame[:,:,2]
                        cv2.imwrite("results/"+ map  + "_near_" + str(i)+".png", f1)
                        cv2.imwrite("results/"+ map  + "_far_" + str(i)+".png", f2)
                        out.write(f1)
                    else:
                        cv2.imwrite("results/"+ map +str(i)+".png", frame)
                        out.write(frame)
                else:
                    print("Numer of frames: " + str((i+1)/2))
                    break
