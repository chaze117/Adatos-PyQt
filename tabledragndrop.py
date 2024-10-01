from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QAbstractItemView, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag

class DraggableTableWidget(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)

    def startDrag(self, supportedActions):
        drag = QDrag(self)
        mime_data = QMimeData()

        selected_items = self.selectedItems()
        if not selected_items:
            return

        # Extract the row of the first selected item
        row = selected_items[0].row()
        
        # Collect all column data for this row
        self.dragged_row_data = [self.item(row, col).text() for col in range(self.columnCount())]
        
        # Set the dragged row data as text in MIME data
        mime_data.setText("\n".join(self.dragged_row_data))
        drag.setMimeData(mime_data)

        # Execute the drag and drop operation
        drop_action = drag.exec(Qt.DropAction.MoveAction)

        # Remove the row if the drag operation was successful
        if drop_action == Qt.DropAction.MoveAction:
            self.removeRow(row)

    def dragEnterEvent(self, event):
        if event.source() != self:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if event.source() == self:
            event.ignore()
            return

        # Retrieve the dropped data as a list of strings
        dropped_text = event.mimeData().text().splitlines()
        
        # Add the dropped data as a new row
        row_position = self.rowCount()
        self.setRowCount(row_position + 1)
        
        for column, text in enumerate(dropped_text):
            self.setItem(row_position, column, QTableWidgetItem(text))
            print(text)

        event.acceptProposedAction()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Drag and Drop with Removal Example")
        self.setGeometry(100, 100, 800, 400)

        # Create two table widgets
        self.table1 = DraggableTableWidget(5, 3)
        self.table2 = DraggableTableWidget(0, 3)

        # Populate the first table with sample data
        for row in range(5):
            for col in range(3):
                self.table1.setItem(row, col, QTableWidgetItem(f"Item {row + 1}-{col + 1}"))

        # Create a layout and add the tables
        layout = QHBoxLayout()
        layout.addWidget(self.table1)
        layout.addWidget(self.table2)

        # Create a central widget for the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
