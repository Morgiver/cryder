from ApplicationClass import Application
from Components.MainComponent import MainComponent
from Components.DearPyGUIComponent import DearPyGUIComponent

if __name__ == '__main__':
    app = Application()
    app.use(MainComponent)
    app.use(DearPyGUIComponent)
    app.run()
