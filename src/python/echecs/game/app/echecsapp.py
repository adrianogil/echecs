from .qmlapp import QMLApp


class EchecsApp():
    def __init__(self, *args, **kwargs):
        self.qml_app = QMLApp()
        self.qml_app.main_qml = 'echecs/game/app/qml/echecs/main.qml'

    def show(self):
        self.qml_app.execute()


if __name__ == '__main__':
    app = EchecsApp()
    app.show()
