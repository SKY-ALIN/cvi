"""Скрипт выводит список id доступных камер."""

import cv2
arr = []
for i in range(30):
    cap = cv2.VideoCapture(i)
    if cap.read()[0]:
        arr.append(i)
    cap.release()
print(arr)
