"""Файл с классом и функциями для работы с метками Аруко"""
import numpy as np
import cv2
import cv2.aruco as aruco

class Aruco:
    """Класс для поиска Аруко меток."""

    COLOR = (0, 204, 255)

    def __init__(self, cap):
        """Как аргумент передаём камеру."""

        self.CAP = cap
        # self.CAP.set(3, 1280)
        # self.CAP.set(4, 720)
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        self.parameters =  aruco.DetectorParameters_create()

    def get_markers(self):
        """Функция читает с камеры и возвращает координаты углов и idшники меток"""

        ret, self.frame = self.CAP.read()
        # self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.corners, self.ids, _ = aruco.detectMarkers(self.frame, self.aruco_dict,
                                                        parameters=self.parameters)
        return self.corners, self.ids

    def render_frame(self):
        """Рендерит информацию меток в кадре"""

        markers_frame = aruco.drawDetectedMarkers(self.frame, self.corners, self.ids,
                                                  borderColor=self.COLOR)
        return markers_frame

def aruco_center(corner):
    """Принимает описание координат углов метки, возвращает координаты центра метки."""

    x = (corner[0][0][0] + corner[0][2][0]) / 2
    y = (corner[0][0][1] + corner[0][2][1]) / 2
    return int(x), int(y)

def aruco_angel(corner):
    """Принимает описание координат углов метки, возвращает угол поворота метки."""
    x1 = corner[0][0][0]
    y1 = corner[0][0][1]
    x2 = corner[0][3][0]
    y2 = corner[0][3][1]
    return math.atan2(x2-x1, y2-y1)*180/math.pi
