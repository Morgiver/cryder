from Core import *


class HistoricDataPackage(AbstractPackage):
    def __init__(self, root_app):
        AbstractPackage.__init__(self, root_app, 'HistoricData')

        self.State = None

    def instanciate(self):
        super().instanciate()
        self.State = self.require('State')

