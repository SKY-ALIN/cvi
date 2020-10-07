"""Файл с классом визуализатора."""

from datetime import datetime, timedelta
import numpy as np
import cv2

class Visualizer:
    """Визуализатор внутренних процесов в программах компьютерного зрения."""

    # Параметры отображаемые визуализатором
    VERSION = "VERSION 1.0"
    LABEL = "MADE BY ALINSKY"
    target = "TARGET"
    tasks = []
    texts = []

    # Константы визуализатора. Можно менять для персональной конфигурации.
    COLOR = (0, 204, 255)
    THICKNESS = 1
    INDENTS = 8
    INCLINE = 10
    FONT = cv2.FONT_HERSHEY_SIMPLEX
    SCALE = 1

    notification_flag = False
    notification_text = ''
    notification_time = 0


    def handle(self, frame):
        """Функция отрисовки процессов и параметров в кадре."""

        try:
            height, width, _ = frame.shape
        except ValueError:
            height, width = frame.shape

        # VERSION
        (text_width, text_height), _ = cv2.getTextSize(self.VERSION, self.FONT, self.SCALE,
                                                       cv2.LINE_AA)
        cv2.putText(frame, self.VERSION, (self.INDENTS, height-self.INDENTS), self.FONT, self.SCALE,
                    self.COLOR, self.THICKNESS, cv2.LINE_AA)
        pts = np.array([[0, height-text_height-self.INDENTS],
                        [text_width+self.INDENTS-self.INCLINE, height-text_height-self.INDENTS],
                        [text_width+self.INDENTS+self.INCLINE, height]],
                       np.int32).reshape((-1, 1, 2))
        frame = cv2.polylines(frame, [pts], False, self.COLOR, self.THICKNESS)

        # LABEL
        (text_width, text_height), _ = cv2.getTextSize(self.LABEL, self.FONT, self.SCALE,
                                                       cv2.LINE_AA)
        cv2.putText(frame, self.LABEL, (width-text_width-self.INDENTS, height-self.INDENTS-1),
                    self.FONT, self.SCALE, self.COLOR, self.THICKNESS, cv2.LINE_AA)
        pts = np.array([[width-text_width-self.INDENTS*3-self.INCLINE, height],
                        [width-text_width-self.INDENTS*3+self.INCLINE,
                         height-text_height-self.INDENTS],
                        [width, height-text_height-self.INDENTS]], np.int32).reshape((-1, 1, 2))
        frame = cv2.polylines(frame, [pts], False, self.COLOR, self.THICKNESS)

        # TARGET
        (text_width, text_height), _ = cv2.getTextSize(self.target, self.FONT, self.SCALE+0.5,
                                                       cv2.LINE_AA)
        cv2.putText(frame, self.target, (250, text_height+self.INDENTS), self.FONT, self.SCALE+0.5,
                    self.COLOR, self.THICKNESS+1, cv2.LINE_AA)
        pts = np.array([[250-self.INDENTS*2-self.INCLINE, 0],
                        [250-self.INDENTS*2+self.INCLINE, text_height+self.INDENTS*4],
                        [width, text_height+self.INDENTS*4]],
                       np.int32).reshape((-1, 1, 2))
        frame = cv2.polylines(frame, [pts], False, self.COLOR, self.THICKNESS+1)
        target_height = text_height

        # TASKS
        if self.tasks:
            (text_width, text_height), _ = cv2.getTextSize(max(self.tasks, key=len)+"x. ",
                                                           self.FONT, self.SCALE, cv2.LINE_AA)
            for i, task in enumerate(self.tasks):
                cv2.putText(frame, "{}. {}".format(i+1, task),
                            (width-text_width-self.INDENTS, target_height+self.INDENTS*(5+i)+
                             text_height*(i+1)),
                            self.FONT, self.SCALE, self.COLOR, self.THICKNESS, cv2.LINE_AA)

        # NOTIFICATION
        if self.notification_flag:
            if self.notification_time + timedelta(seconds=5) < datetime.now():
                self.notification_flag = False
            if int(datetime.now().microsecond / 100000) % 2:
                (text_width, text_height), _ = cv2.getTextSize(self.notification_text, self.FONT,
                                                               self.SCALE+0.5, cv2.LINE_AA)
                cv2.putText(frame, self.notification_text,
                            (int((width-text_width)/2), int(height*0.8)), self.FONT,
                            self.SCALE+0.5, self.COLOR, self.THICKNESS+1, cv2.LINE_AA)

        # TEXT
        if self.texts:
            (text_width, text_height), _ = cv2.getTextSize(self.texts[0], self.FONT, self.SCALE/3,
                                                           cv2.LINE_AA)
            for i, text in enumerate(self.texts):
                cv2.putText(frame, text, (5, text_height*(i+1)), self.FONT, self.SCALE/3,
                            self.COLOR, self.THICKNESS, cv2.LINE_AA)

        return frame


    def notify(self, notification):
        """Функция для отправки уведомления в визуализатор."""

        self.notification_flag = True
        self.notification_text = notification
        self.notification_time = datetime.now()


    def record(self, file_name="Unknown.mp4"):
        pass
