import sys

import win32con
import win32gui
from PyQt5 import QtCore, Qt
from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QPoint
from PySide2.QtCore import *
WINDOW_SIZE = 0
class TaskBarManagement():


    def __init__(self):
        self.flag = 0
        self.frameless = QtCore.Qt.FramelessWindowHint

    def close(self):
        sys.exit()

    def minimize(self):
        mini = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(mini, win32con.SW_MINIMIZE)



    def zoom(self):
        # Global windows state
         #The default value is zero to show that the size is not maximized
        global WINDOW_SIZE
        win_status = WINDOW_SIZE

        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1  # Update value to show that the window has been maxmized
            full = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(full, win32con.SW_MAXIMIZE)

        else:
            # If the window is on its default size
            WINDOW_SIZE = 0
            full = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(full, win32con.SW_SHOWNORMAL)






