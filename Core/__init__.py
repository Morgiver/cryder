import sys


class AbstractPackage:
    def __init__(self, root_app, name):
        self.root_app = root_app
        self.name = name
        print(f'[{self.name}] is Registered')

    def instantiate(self):
        print(f'Instantiation of {self.name}')

    def require(self, package_name):
        return self.root_app.require(package_name)


class RootApplication:
    def __init__(self):
        self.packages = {}

        self.register_package("State")
        self.register_package("Exchanges")
        self.register_package("Database")
        self.register_package("HistoricData")
        self.register_package("AI")
        self.register_package("UI")

        self.instantiate_package()

    @staticmethod
    def __import__(package_name):
        try:
            package = __import__(package_name)
            main_class = getattr(package, f'{package_name}Package')
            return main_class
        except ModuleNotFoundError:
            print(f"{package_name} does not exist")
        except:
            print("Unexpected error :", sys.exc_info()[0])

    def register_package(self, package_name):
        package_class = self.__import__(package_name)
        package = package_class(self)
        self.packages[package.name] = package

    def instantiate_package(self):
        for package in self.packages:
            self.packages[package].instantiate()

    def require(self, package_name):
        try:
            return self.packages[package_name]
        except KeyError:
            print(f"Package Error : [{package_name}] is not Registred")
        except:
            print("Unexpected error :", sys.exc_info()[0])

