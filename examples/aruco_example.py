"""Пример работы с метками Аруко."""

import numpy as np
import math
import cv2
from cvi import Aruco, aruco_center, aruco_angel
from cvi import Visualizer

def data(corner):
    """Функция возвращает данные о метке в читабельном формате."""
    x, y = aruco_center(corner)
    return "x = {}; y = {}; angel = {}".format(x, y, round(aruco_angel(corner), 2))

# Объявляем камеру
cap = cv2.VideoCapture(0)
aruco = Aruco(cap)

# Объявляем визуализатор
visualizer = Visualizer()
visualizer.target = "Aruco markers"

while cap.isOpened():
    # Получаем информацию о наблюдаемых метках
    corners, ids = aruco.get_markers()

    # Обнуляем данные визуализатора
    visualizer.tasks = []
    visualizer.texts = []

    # Если наблюдаем какие-то метки, то заносим информацию в визуализатор
    if type(ids) == np.ndarray:
        for id in ids:
            visualizer.tasks.append("Marker with id {}".format(id[0]))
        for corner in corners:
            visualizer.texts.append(data(corner))

    # Отображаем
    cv2.imshow('Aruco markers example', visualizer.handle(aruco.render_frame()))

    # Для завершения при нажатии на клавишу "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
