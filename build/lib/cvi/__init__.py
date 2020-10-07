"""CVI - Computer Vision Interface.

Модуль упрощает работу с библиотекой компьютерногого зрения OpenCV. В модуль включён визуализатор
который позволяет удобно отображать процессы происходящие внутри программы и аруко метки.
"""

from .visualizer import Visualizer
from .aruco import Aruco, aruco_center, aruco_angel

__version__ = '1.1.0'
