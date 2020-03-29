import numpy as np
import math
import cv2
from cvi import Aruco, aruco_center, aruco_angel
from cvi import Visualizer

def data(corner):
    x, y = aruco_center(corner)
    return "x = {}; y = {}; angel = {}".format(x, y, round(aruco_angel(corner), 2))

cap = cv2.VideoCapture(0)
aruco = Aruco(cap)
visualizer = Visualizer()
visualizer.target = "Aruco markers"

while 1:
    corners, ids = aruco.get_markers()

    visualizer.tasks = []
    visualizer.texts = []
    if type(ids) == np.ndarray:
        for id in ids:
            visualizer.tasks.append("Marker with id {}".format(id[0]))
        for corner in corners:
            visualizer.texts.append(data(corner))

    cv2.imshow('Aruco markers example', visualizer.handle(aruco.render_frame()))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
