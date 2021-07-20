import sys
from PySide2.QtCore import QDir, QObject, QUrl, Signal, Slot
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PySide2.QtWidgets import QApplication, QMainWindow


class WebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        QWebEnginePage.__init__(self, parent)

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceId):
        print('js', level, message, lineNumber, sourceId)


# partly based on https://stackoverflow.com/a/50610834/6872193
class Backend(QObject):
    signal = Signal('QVariant')

    def __init__(self, parent=None):
        QObject.__init__(self, parent)

    @Slot()
    def load_table(self):
        self.signal.emit('table')


class WebView(QWebEngineView):
    def __init__(self, parent=None):
        QWebEngineView.__init__(self, parent)
        self.setPage(WebEnginePage(self))

    def contextMenuEvent(self, event):
        pass


class AppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1500, 900)
        self.view = WebView(self)
        self.page = self.view.page()
        self.backend = Backend(self.view)
        channel = QWebChannel(self)
        self.page.setWebChannel(channel)
        channel.registerObject('backend', self.backend)
        self.view.load(QUrl.fromLocalFile(QDir.current().filePath('main.html')))
        self.setCentralWidget(self.view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
