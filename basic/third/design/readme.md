Для конвертации Qt `*.ui` файлов в исполняемый Python-код выполним команду:

```
pyuic5 window.ui -o window.py
```

Для быстрого создания приложения с загрузкой дизайна, используем пример:

```
import sys
from PyQt5 import QtWidgets
from design import window


class ExampleApp(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
```