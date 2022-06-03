import gpxpy
import glob
import numpy as np
import cv2
import mat

files=glob.glob("activities/*.gpx")



class Run:
    def __init__(self,gpxData) -> None:
        self.gpxData = gpxData

        self.points=[]
        for track in self.gpxData.tracks:
            for segment in track.segments:
                for point in segment.points:
                    self.points.append(point)

        self.points.sort(key=lambda x: x.time)
    
    def draw(self,image):
        


runs=[]
for file in files[0:5]:
    try:
        gpxData=gpxpy.parse(open(file))
    except Exception:
        print(f"{file} failed")

    runs.append(Run(gpxData))

for run in runs:
    blank=np.zeros((800,800,3))
    blank[::]=127

    cv2.imshow("window",blank)
    cv2.waitKey(0)
    