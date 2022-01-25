import os
from subprocess import check_call, check_output
from multiprocessing.dummy import Pool



"""
Sequence Settings
"""
sequence_path = "/home/michael/Documents/mpeg_datasets/CfP/datasets/Dynamic_Objects/People/8i/8iVFBv2"
target_path = "/home/michael/Documents/vpcc_ours_encoded/"
objects = [
#        "longdress/",
#        "loot",
#        "redandblack",
        "soldier"
        ]
offsets = {
        "longdress" : 1051,
        "loot" : 1000,
        "redandblack" : 1450,
        "soldier" : 536
        }
qualities = [
        "ctc-r1.cfg",
        "ctc-r2.cfg",
        "ctc-r3.cfg",
        "ctc-r4.cfg",
        "ctc-r5.cfg"
        ]
frames_per_segment = 30 # Total number of segments for encoding
orientation_separation = False #If seperation of streams or not is wanted

log_file = "UEQLog.txt"
""" 
Encoder Settings
"""

encoder_path = "/home/michael/Documents/Software/VPCC/mpeg-pcc-tmc2/bin/PccAppEncoder"
video_encoder_path = "/home/michael/Documents/Software/VPCC/external/HM/bin/TAppEncoderStatic"
color_space_conversion_path = "/home/michael/Documents/Software/VPCC/external/HDRTools/bin/HDRConvert"
config_path = "/home/michael/Documents/Software/VPCC/mpeg-pcc-tmc2/cfg/"

standard_settings = "--additionalProjectionPlaneMode=0 \
--constrainedPack \
--packingStrategy=2"



"""
Multiprocessing
"""
def call_command(command):
    ret_val = check_output(command, shell=True)
    with open(log_file, "a") as file:
        if ret_val == 0:
            file.write("Successfully completed command: \n" + command + "\n\n")
        else:
            file.write("Error with command: \n" + command + "\n\n")

"""
Script
"""

if not os.path.exists(target_path):
    print("Path not existant")
    exit(0)

pool = Pool(4)

commands = []
for obj in objects:
    obj_path = os.path.join(sequence_path, obj, "Ply")
    obj_list = os.listdir(obj_path)
    obj_list.sort()
    for i, quality in enumerate(qualities):
        save_to_path = os.path.join(os.path.join(target_path, obj), str(i+1))
        if not os.path.exists(save_to_path):
            os.makedirs(save_to_path)
        for j, start_frame in enumerate(range(0, 300, frames_per_segment)):
            print("Encoding frames " + str(start_frame) + " to " + str(start_frame + frames_per_segment - 1))

            start_ply = obj_list[start_frame]
            print("Starting with " + str(start_ply))

            command = encoder_path
            command += " --configurationFolder=" + config_path
            command += " --config=" + os.path.join(config_path, "common/ctc-common.cfg")
            command += " --config=" + os.path.join(config_path, "condition/ctc-all-intra.cfg")
            command += " --config=" + os.path.join(config_path, "sequence/" + obj + "_vox10.cfg")
            command += " --config=" + os.path.join(config_path, "rate/" + quality)
            command += " --startFrameNumber=" + str(start_frame + offsets[obj])
            command += " " + standard_settings
            command += " --videoEncoderOccupancyPath=" + video_encoder_path
            command += " --videoEncoderAttributePath=" + video_encoder_path
            command += " --videoEncoderGeometryPath=" + video_encoder_path
            command += " --colorSpaceConversionPath=" + color_space_conversion_path
            command += " --uncompressedDataFolder=" + os.path.dirname(os.path.dirname(sequence_path)) + "/"
            command += " --frameCount=" + str(frames_per_segment)
            command += " --compressedStreamPath=" + os.path.join(save_to_path, "segment_" + str(j) + ".bin")
            command += " --reconstructedDataPath=" + os.path.join(save_to_path, "rec_%04d.ply")


            if orientation_separation:
                command += " --orientationSeparation"
            print(command)

            #append command if outputfile is not existant
            if not os.path.exists(os.path.join(save_to_path, "segment_" + str(j) + ".bin")):
                commands.append(command)
            else:
                with open(log_file, "a") as file:
                    file.write("Skipping " + save_to_path + " - Segment" + str(j) + "\n")

pool.map(call_command, commands)
pool.close()
pool.join()
