
class Test:
    def __init__(self):
        print('Classe Test')

    def do(self, name, kwargs):
        method = getattr(self, f'{name}Action')
        method(**kwargs)

    def receive(self, message):
        try:
            self.do(message['name'], message["params"])
        except AttributeError as error:
            print(error)

    def printAction(self, to_print, to_print_two):
        print(to_print)
        print(to_print_two)


c = Test()
message = {
    "name": "print",
    "params": { 'to_print': 'mon premier message', 'to_print_two': 'Et sa suite' }
}
c.receive(message)
