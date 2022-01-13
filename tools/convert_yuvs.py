import cv2
from videoCapture import VideoCapture
import os
import sys
import re

def getInfoFromFilename(filename):
    '''
    Some sketchy regex stuff for getting infos from file name
    '''
    size = re.findall(r"_\d{2,4}x\d{2,4}_", filename)[0][1:-1].split("x")
    size = [int(s) for s in size]
    atlas = int(re.findall(r"Orientation_\d{1,2}_", filename)[0][12:-1])
    print("found")
    gof = int(re.findall(r"GOF\d{1,2}", filename)[0][3:])

    return size, atlas, gof

def filterDir(directory, mapInfo):
    files = os.listdir(directory)
    files = [file for file in files if '.yuv' in file] # YUV files
    files = [file for file in files if mapInfo in file] # Occupancy maps
    files = [file for file in files if 'rec' not in file] # orignals
    return files

def createOccVideo(filename):
    size, atlas, gof = getInfoFromFilename(filename)
    videoPath = 'results/vid_occupancy_' + str(atlas) + '_' + str(gof) + '.avi'
    cap = VideoCapture(filename, size, convert=False)
    out = cv2.VideoWriter(videoPath, 
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 
                          5, 
                          (size[0], size[1]))

    i = 0
    while 1:
        ret, frame = cap.read()
        if not ret:
            print(filename + " converted. #Frames: " + str(i))
            break
        frame = frame[:size[1], :size[0]]
        filePath = "results/occupancy_ " + str(gof) +"_" \
                + str(i)+ "_" + str(atlas) + ".png"
        cv2.imwrite(filePath, frame * 255)
        frame = cv2.cvtColor(frame*255, cv2.COLOR_GRAY2BGR)
        out.write(frame)
        i = i+1


def createGeoVideo(filename):
    size, atlas, gof = getInfoFromFilename(filename)
    videoPath = 'results/vid_geometry_' + str(atlas) + '_' + str(gof) + '.avi'
    cap = VideoCapture(filename, size, convert=True)
    out = cv2.VideoWriter(videoPath, 
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 
                          5, 
                          (size[0], size[1]))

    i = 0
    while 1:
        ret, frame = cap.read()
        if not ret:
            print(filename + " converted. #Frames: " + str(i))
            break

        f1 = frame[:,:,1]
        f2 = frame[:,:,2]
        f1 = cv2.cvtColor(f1, cv2.COLOR_GRAY2BGR)
        f2 = cv2.cvtColor(f2, cv2.COLOR_GRAY2BGR)
        cv2.imwrite("results/geomtery_" + str(gof)  + "_near_" + str(i) + "_" + str(atlas) +".png", f1)
        cv2.imwrite("results/geomtery_" + str(gof)  + "_far_" + str(i) + "_" + str(atlas) +".png", f2)
        out.write(f1)
        i = i+1
        
def createAttVideo(filename):
    size, atlas, gof = getInfoFromFilename(filename)
    videoPath = 'results/vid_attribute_' + str(atlas) + '_' + str(gof) + '.avi'
    cap = VideoCapture(filename, size, convert=True)
    out = cv2.VideoWriter(videoPath, 
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 
                          5, 
                          (size[0], size[1]))
    i = 0
    while 1:
        ret, frame = cap.read()
        if not ret:
            print(filename + " converted. #Frames: " + str(i))
            break

        cv2.imwrite("results/attribute_"+ str(gof) + "_" + str(i)+ "_" + str(atlas) + ".png", frame)
        out.write(frame)
        i = i+1

def createVideos(directory):
    files = filterDir(directory, 'occupancy')
    for filename in files:
        createOccVideo(filename)

    files = filterDir(directory, 'attribute')
    for filename in files:
        createAttVideo(filename)

    files = filterDir(directory, 'geometry')
    for filename in files:
        createGeoVideo(filename)




if __name__ == '__main__':
    print("Start")
    directory = os.chdir('/home/michael/Documents/Software/VPCC/mpeg-pcc-tmc2')

    createVideos(directory)
