from PySide6.QtWidgets import (
    QWidget,  # 窗口
    QVBoxLayout,  # 垂直布局
    QPushButton  # 按钮，用于触发操作
)
from PySide6.QtGui import QFont

from renamer.batch_file_renamer import RenameFileApp


# 主窗口类
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyQt示例应用')
        self.setGeometry(100, 100, 300, 250)  # 设置窗口的位置和大小
        self.setStyleSheet('background-color: #F5F5F5;')  # 设置窗口背景色为淡灰色

        layout = QVBoxLayout()  # 创建一个垂直布局

        # 重命名使者
        rename_file_btn = QPushButton('重命名使者')  # 创建按钮
        rename_file_btn.setFont(QFont('Arial', 14))
        rename_file_btn.setStyleSheet('''
            QPushButton {
                background-color: #9C27B0;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #8E24AA;
            }
        ''')

        rename_file_btn.clicked.connect(self.rename_file_btn_clicked)  # 连接点击事件

        layout.addWidget(rename_file_btn)  # 将按钮添加到垂直布局中

        self.setLayout(layout)  # 将布局应用到窗口

    def rename_file_btn_clicked(self):
        print('按钮<重命名使者>被点击了')
        self.rename_file = RenameFileApp()  # noqa
        self.rename_file.show()  # 打开另一个窗口
