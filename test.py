from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class ToggleButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("OFF", parent)
        self.setCheckable(True)  # Allows the button to have checked/unchecked states
        self.setFixedSize(100, 40)
        self.setStyleSheet(self.get_stylesheet(False))

        # Connect the toggled signal to handle state change
        self.toggled.connect(self.on_toggled)

    def on_toggled(self, checked):
        self.setText("ON" if checked else "OFF")
        self.setStyleSheet(self.get_stylesheet(checked))
        print("Toggle is ON" if checked else "Toggle is OFF")

    def get_stylesheet(self, checked):
        if checked:
            return """
                QPushButton {
                    background-color: green;
                    color: white;
                    border: 2px solid #5A5A5A;
                    border-radius: 20px;
                }
            """
        else:
            return """
                QPushButton {
                    background-color: lightgray;
                    color: black;
                    border: 2px solid #5A5A5A;
                    border-radius: 20px;
                }
            """

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Toggle Button Example")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()
        
        # Create a toggle button and add it to the layout
        toggle_button = ToggleButton(self)
        layout.addWidget(toggle_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()



