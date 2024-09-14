import sys

from PyQt6 import QtCore, QtWidgets, QtWebEngineWidgets
import PyQt6

def main():

    print(
        f"PyQt6 version: {QtCore.PYQT_VERSION_STR}, Qt version: {QtCore.QT_VERSION_STR}"
    )

    app = QtWidgets.QApplication(sys.argv)
    filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, filter="PDF (*.pdf)")
    if not filename:
        print("please select the .pdf file")
        sys.exit(0)
    view = QtWebEngineWidgets.QWebEngineView()
    settings = view.settings()
    settings.setAttribute(view.settings().WebAttribute.PluginsEnabled, True)
    url = QtCore.QUrl.fromLocalFile(filename)
    view.load(url)
    view.resize(640, 480)
    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
