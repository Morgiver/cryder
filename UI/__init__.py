from Core import *
SEND_TO_ALL = "All"


class Mediator:
    def __init__(self):
        self.subscribers = {}

    def register(self, ui_subscriber_class, name):
        subscriber = ui_subscriber_class(self, name)
        self.subscribers[subscriber.name] = subscriber
        return self.subscribers[subscriber.name]

    def send(self, message, sender, receiver=SEND_TO_ALL):
        if receiver == SEND_TO_ALL:
            for sub in self.subscribers:
                self.subscribers[sub].receive(message, sender)
        elif isinstance(receiver, list):
            for sub in sender:
                self.subscribers[sub].receive(message, sender)
        elif isinstance(receiver, str):
            self.subscribers[sender].receive(message, sender)


class AbstractUISubscriber:
    def __init__(self, name, mediator):
        self.mediator = mediator
        self.name = name

    def send(self, message, receiver=SEND_TO_ALL):
        self.mediator.send(message, self, receiver)

    def receive(self, sender, message):
        try:
            method = getattr(self, f'{message.method_name}Action')
            method(sender, **message.params)
        except AttributeError as error:
            print(error)


class UIPackage(AbstractPackage):
    def __init__(self, root_app):
        AbstractPackage.__init__(self, root_app, 'UI')

        self.mediator = Mediator()

    def add_ui_subscriber(self, subscriber_class, name):
        self.mediator.register(subscriber_class, name)
