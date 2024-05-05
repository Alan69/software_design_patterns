# Model
class Model:
    def __init__(self):
        self._data = None

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

# View
class View:
    def show_data(self, data):
        print("View: Data is", data)

# Controller
class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def update_data(self, data):
        self._model.set_data(data)
        self._view.show_data(self._model.get_data())

# Client code
if __name__ == "__main__":
    # Create instances of model, view, and controller
    model = Model()
    view = View()
    controller = Controller(model, view)

    # Update data using controller
    controller.update_data("New data")
