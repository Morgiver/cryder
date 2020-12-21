import dearpygui.core as core
import dearpygui.simple as simple
from AbstractApplication import AbstractComponent


class AbstractWindow:
    def __init__(self, name):
        self.name = name
        self.core = core
        self.simple = simple

    def render(self, sender, data, states):
        pass

    def show(self, context):
        pass


class DearPyGUIComponent(AbstractComponent):
    def __init__(self, root):
        self.data = {
            "main_window": "MainWindow",
            "windows": []
        }

        super().__init__("DearPyGUI", root)

    def render_action(self, context, payload):
        for i in range(len(self.state.windows)):
            self.state.windows[i].render(payload.sender, payload.data, context.states)

    def open_window_action(self, context, payload):
        window = payload.window(context, **payload.parameters)
        window.show()
        context.commit('DearPyGUI.add_window', {"window": window})

    def start_dear_action(self, context, payload):
        core.set_render_callback(lambda sender, data: context.dispatch("DearPyGUI.render", {
            "sender": sender,
            "data": data
        }))

        core.start_dearpygui(primary_window=self.state.main_window)

    def add_window_mutation(self, context, payload):
        self.state.windows.append(payload.window)

    def start_action_listener(self, context, payload):
        context.dispatch('DearPyGUI.start_dear', {})

