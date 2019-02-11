from imageai.Detection import VideoObjectDetection
import os
import cv2
import subprocess

def runcv():
    
    camera = cv2.VideoCapture(0)

    detector = VideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("C:\\Users\\ExMiracle\\Downloads\\yolo.h5")
    detector.loadModel()

    video = detector.detectObjectsFromVideo(camera_input=camera, save_detected_video=False
        , frames_per_second=20, log_progress=True, minimum_percentage_probability=30)

##    print(video_path)
    p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe", video])
                     
    p
