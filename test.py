# import sys

# from PyQt6 import QtCore, QtWidgets, QtWebEngineWidgets
# import PyQt6

# def main():

#     print(
#         f"PyQt6 version: {QtCore.PYQT_VERSION_STR}, Qt version: {QtCore.QT_VERSION_STR}"
#     )

#     app = QtWidgets.QApplication(sys.argv)
#     filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, filter="PDF (*.pdf)")
#     if not filename:
#         print("please select the .pdf file")
#         sys.exit(0)
#     view = QtWebEngineWidgets.QWebEngineView()
#     settings = view.settings()
#     settings.setAttribute(view.settings().WebAttribute.PluginsEnabled, True)
#     settings.setAttribute(view.settings().WebAttribute.PdfViewerEnabled, True)
#     settings.setAttribute(view.settings().WebAttribute.JavascriptCanOpenWindows, True)
#     settings.setAttribute(view.settings().WebAttribute.PrintElementBackgrounds, True)
#     url = QtCore.QUrl.fromLocalFile(filename)
#     view.load(url)
#     view.resize(640, 480)
#     view.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()
import sys
import os
import win32api
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtCore import QUrl

class PDFViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Viewer with Print Support")
        self.setGeometry(100, 100, 800, 600)

        # Create layout
        layout = QVBoxLayout()

        # Create a QWebEngineView widget to display the PDF
        self.web_view = QWebEngineView()

        # Enable necessary settings for the web view
        self.configure_web_view()

        # Add the web view to the layout
        layout.addWidget(self.web_view)

        # Create a button to load a PDF file
        self.open_button = QPushButton("Open PDF")
        self.open_button.clicked.connect(self.open_pdf)
        layout.addWidget(self.open_button)

        # Create a button to trigger printing
        self.print_button = QPushButton("Print PDF")
        self.print_button.clicked.connect(self.print_pdf)
        layout.addWidget(self.print_button)

        # Create a central widget and set the layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Store the current file path
        self.current_pdf_file = ""

        # Connect the printRequested signal from the web page to handle print requests
        self.web_view.page().printRequested.connect(self.handle_print_requested)

    def configure_web_view(self):
        # Configure settings for QWebEngineView to enable PDF handling and advanced features
        settings = self.web_view.settings()
        settings.setAttribute(settings.WebAttribute.PluginsEnabled, True)
        settings.setAttribute(settings.WebAttribute.PdfViewerEnabled, True)
        settings.setAttribute(settings.WebAttribute.JavascriptCanOpenWindows, True)
        settings.setAttribute(settings.WebAttribute.PrintElementBackgrounds, True)

    def open_pdf(self):
        # Open a file dialog to select a PDF file
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if file_name:
            # Use QWebEngineView to load the PDF file
            self.web_view.setUrl(QUrl.fromLocalFile(file_name))
            self.current_pdf_file = file_name  # Store the current PDF file path

    def handle_print_requested(self):
        """Handles the print request from within the web view (triggered by JavaScript)."""
        if not self.current_pdf_file:
            print("No PDF file loaded for printing.")
            return

        # Show print dialog
        self.show_print_dialog()

    def show_print_dialog(self):
        """Shows a print dialog and prints the file."""
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.print_file_with_printer()

    def print_file_with_printer(self):
        """Prints the file using pywin32 with the selected printer settings."""
        # Ensure the file exists
        if not os.path.exists(self.current_pdf_file):
            print(f"File {self.current_pdf_file} does not exist.")
            return

        # Use win32api to send the file to the selected printer
        # ShellExecute will use the default printer settings
        win32api.ShellExecute(0, "print", self.current_pdf_file, None, ".", 0)

    def print_pdf(self):
        """Manually triggers the print dialog."""
        if not self.current_pdf_file:
            print("No PDF file loaded for printing.")
            return

        self.show_print_dialog()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = PDFViewer()
    viewer.show()
    sys.exit(app.exec())
