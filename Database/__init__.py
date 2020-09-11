from Core import *


class DatabasePackage(AbstractPackage):
    def __init__(self, root_app):
        AbstractPackage.__init__(self, root_app, "Database")

