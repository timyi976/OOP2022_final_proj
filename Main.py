from View import view
from Control import Controller
from Model import model

class app():
    def __init__(self):
        self.controller = Controller()
        self.view = view()
        self.view.set_controller(self.controller)

if __name__ == '__main__':
    app = app()
    app.view.start_ui()