from AbstractApplication import *
from DearPyGUIComponent import AbstractWindow


class MainWindow(AbstractWindow):
    def __init__(self):
        super().__init__("MainWindow")

    def show(self, context):
        with self.simple.window(self.name):
            pass


class MainComponent(AbstractComponent):
    def __init__(self, root):
        self.data = {}

        super().__init__("Main", root)

    def start_action(self, context, payload):
        context.dispatch("DearPyGUI.open_window", {"window": MainWindow, "parameters": {}})