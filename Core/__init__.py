
class AbstractPackage:
    def __init__(self, root_app, name):
        self.root_app = root_app
        self.name = name
        print(f'[{self.name}] is Registered')

    def instantiate(self):
        print(f'Instantiation of {self.name}')

    def require(self, package_name):
        return self.root_app.require(package_name)

