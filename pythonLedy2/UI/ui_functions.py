
from main import *

class FunctionsUI(MainWindow):
    def name_of_button_clicked(self):
        print("aaa")
        try:
            nadawca = self.ui.sender()
        except Exception as e:
            print(e)
        print(nadawca.text())
        print("szisz")