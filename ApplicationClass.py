import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from Builders import WindowsBuilder


class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        self._windows = []
        self._models = {}

    def create_window(self, name="MainWindow", **kwargs):
        self._windows.append(WindowsBuilder.build(app_instance=self, class_name=name, **kwargs))
        self._windows[-1].show()

    def run(self):
        self.create_window(
            name="MainWindow",
            setWindowTitle="CryDer",
            setMinimumSize=QSize(400, 240),
            resize=QSize(800, 600),
            setStyleSheet="QMainWindow { background-color: #282828; }"
        )
        self.exec_()
