"""Пример работы визуализатора."""

from datetime import datetime
import cv2
from cvi import Visualizer

visualizer = Visualizer()

# Конфигурируем камеру
cam = cv2.VideoCapture(0)
cam.set(3, 1280)
cam.set(4, 720)

# Отправляем уведомление
visualizer.notify("Notification")

while cam.isOpened():
    # Считываем с камеры кадр
    ret, frame = cam.read()

    # Выставляем задачу в визуализатор
    visualizer.tasks = ["Painting"]
    # Выставляем текст в визуализатор. 1 строка = 1 элемент списка
    visualizer.texts = [str(datetime.now()),
                        "FPS is {}".format(cam.get(cv2.CAP_PROP_FPS)),
                        "Size is {} x {}".format(cam.get(3), cam.get(4))]

    # Отрисовываем информацию
    img = visualizer.handle(frame)
    # Выводим результат на экран
    cv2.imshow('frame', img)

    # При нажатии на клавишу q завершаем программу
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
