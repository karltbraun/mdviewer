import sys

import markdown
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QTextBrowser,
)


class MDViewer(QMainWindow):
    """
    MDViewer-ktb: Simple Markdown Viewer

    Usage:
        1. Ensure you have Python 3.8+ and PySide6 installed (see requirements).
        2. Run the application from the command line:
            python src/main.py
        3. Use the File > Open menu to select and view a Markdown (.md) file.
        4. The file will be rendered as HTML in the main window.

    Launching from Finder (macOS):
        - Double-click main.py if Python is associated with .py files, or
        - Right-click main.py, choose "Open With" > "Python Launcher" (or your Python interpreter)
        - Alternatively, create a .command or .app launcher script for easier double-click launching

    Features:
        - Minimal, clean UI
        - Open and view Markdown files
        - Render Markdown as HTML
        - Simple File menu (Open, Exit)

    Requirements:
        - Python 3.8+
        - PySide6
        - markdown

    """

    def __init__(self, initial_file=None):
        super().__init__()
        self.setWindowTitle("MDViewer-ktb")
        self.setGeometry(100, 100, 800, 600)
        self.text_browser = QTextBrowser(self)
        self.setCentralWidget(self.text_browser)
        self._create_menu()
        if initial_file:
            self.load_file(initial_file)

    def _create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Markdown File",
            "",
            "Markdown Files (*.md);;All Files (*)",
        )
        if file_path:
            self.load_file(file_path)

    def load_file(self, file_path):
        import os

        if not os.path.isfile(file_path):
            import sys

            print(
                f"Error: File does not exist: {file_path}", file=sys.stderr
            )
            sys.exit(1)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                md_text = f.read()
                html = markdown.markdown(md_text)
                self.text_browser.setHtml(html)
        except Exception as e:
            self.text_browser.setPlainText(f"Error loading file: {e}")


if __name__ == "__main__":
    import sys

    initial_file = sys.argv[1] if len(sys.argv) > 1 else None
    app = QApplication(sys.argv)
    viewer = MDViewer(initial_file=initial_file)
    viewer.show()
    sys.exit(app.exec())
