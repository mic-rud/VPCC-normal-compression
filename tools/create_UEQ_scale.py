import os
import subprocess


"""
Sequence Settings
"""
sequence_path = "/home/michael/Documents/mpeg_datasets/CfP/datasets/Dynamic_Objects/People/8i/8iVFBv2"
target_path = "/home/michael/Documents/vpcc_ours_encoded/"
objects = [
        "longdress/",
        "loot",
        "redandblack",
        "soldier"
        ]
qualities = [
        "ctc-r1.cfg",
        "ctc-r2.cfg",
        "ctc-r3.cfg",
        "ctc-r4.cfg",
        "ctc-r5.cfg"
        ]
frames_per_segment = 30 # Total number of segments for encoding


""" 
Encoder Settings
"""
encoder_path = "/home/michael/Documents/Software/VPCC/mpeg-pcc-tmc2/bin/PccAppEncoder"


"""
Script
"""

if not os.path.exists(target_path):
    print("Path not existant")
    exit(0)

for obj in objects:
    obj_path = os.path.join(sequence_path, obj, "Ply")
    obj_list = os.listdir(obj_path)
    obj_list.sort()
    print(obj_list)
    for quality in qualities:
        for start_frame in range(0, 300, frames_per_segment):
            print("Encoding frames " + str(start_frame) + " to " + str(start_frame + frames_per_segment - 1))

            start_ply = obj_list[start_frame]
            print("Starting with " + str(start_ply))



