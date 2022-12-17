from audioop import avg
import gpxpy
import glob
import numpy as np
import cv2
import matplotlib
import math


import matplotlib.pyplot as plt





def GPXDistance(point1,point2):
    return math.sqrt((point1.longitude-point2.longitude)**2+(point1.latitude-point2.latitude)**2)

class Run:
    def __init__(self,gpxData) -> None:
        self.gpxData = gpxData

        self.points=[]
        avgLat=0
        avgLon=0
        for track in self.gpxData.tracks:
            for segment in track.segments:
                for point in segment.points:
                    self.points.append(point)
                    avgLat+=point.latitude
                    avgLon+=point.longitude
        
        self.center=gpxpy.gpx.GPXTrackPoint(avgLat/len(self.points), avgLon/len(self.points))
        self.points.sort(key=lambda x: x.time)
        self.start=self.points[0].time
    
    def plot(self):
        Xs=[point.latitude for point in self.points]
        Ys=[point.longitude for point in self.points]
        color=plt.cm.rainbow((hash(self.center)%256)/256)
        plt.plot(Xs,Ys,c=color)

        #plt.scatter
    def draw(self,image):
        pass
        

files=glob.glob("activities/*.gpx")

runs=[]
for file in files:
    try:
        gpxData=gpxpy.parse(open(file))
    except Exception as e:
        print(f"{file} failed {e}")

    run=Run(gpxData)

    center=gpxpy.gpx.GPXTrackPoint(41,-72)


    if(GPXDistance(center,run.center)<2):
        runs.append(run)

    runs.sort(key=lambda x: x.start)

for max in range(len(runs)):
    print(f"{max}/{len(runs)}")
    for run in runs[0:max]:
        blank=np.zeros((800,800,3))
        blank[::]=127

        run.plot()
    plt.savefig(f"fig-{max}.png")

    