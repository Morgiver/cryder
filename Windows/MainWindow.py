from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, root_app):
        super().__init__()

        self._root_app = root_app
