import sys

from PySide6.QtWidgets import QApplication

from renamer.main_window import MainWindow


def main():
    app = QApplication(sys.argv)  # 创建Qt应用上下文

    window = MainWindow()  # 初始化主窗口
    window.setMinimumSize(300, 250)  # 设置窗口最小尺寸
    window.show()

    sys.exit(app.exec())  # 进入事件循环


if __name__ == '__main__':
    main()
