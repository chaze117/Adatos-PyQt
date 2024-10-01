import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QSplashScreen
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        label = QLabel("Welcome to the Main Window!")
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

def main():
    app = QApplication(sys.argv)

    # Create and show the splash screen
    splash_pix = QPixmap('splash_image.png')  # Path to your splash image
    splash = QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())  # Optional: to create a transparent mask
    splash.show()

    # Create the main window
    main_window = MainWindow()

    # Set a timer to close the splash screen and show the main window
    QTimer.singleShot(3000, lambda: [splash.close(), main_window.show()])  # Show splash for 3 seconds

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
