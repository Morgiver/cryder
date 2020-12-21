from AbstractApplication import *


class Application(AbstractApplication):
    def __init__(self):
        super().__init__()

    def run(self):
        self.dispatch("Main.start", {})

