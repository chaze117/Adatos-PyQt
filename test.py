from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Custom Icon Example")
        
        # Set the custom taskbar icon
        self.setWindowIcon(QIcon("icon.ico"))  # Ensure this path is correct

        # Set window size
        self.setGeometry(100, 100, 400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()

    # Show the main window
    window.show()

    # Run the application
    sys.exit(app.exec())