from PyQt5.QtWidgets import (
    QApplication,
    QLineEdit,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Calculator")
        self.setFixedSize(450,270)
        
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Enter mathematical operations: ')
        
        self.h_box = QHBoxLayout()
        
        self.h1_box = QHBoxLayout()
        self.h2_box = QHBoxLayout()
        self.h3_box = QHBoxLayout()
        self.h4_box = QHBoxLayout()
        
        self.v_box = QVBoxLayout()
        
        self.enter_operation = QLineEdit()
        
        self.btn_num_1 = QPushButton('1', self)
        self.btn_num_2 = QPushButton('2', self)
        self.btn_num_3 = QPushButton('3', self)
        self.btn_num_4 = QPushButton('4', self)
        self.btn_num_5 = QPushButton('5', self)
        self.btn_num_6 = QPushButton('6', self)
        self.btn_num_7 = QPushButton('7', self)
        self.btn_num_8 = QPushButton('8', self)
        self.btn_num_9 = QPushButton('9', self)
        self.btn_num_0 = QPushButton('0', self)
        
        self.btn_slash = QPushButton('/', self)
        self.btn_star = QPushButton('*', self)
        self.btn_minus = QPushButton('-', self)
        self.btn_plus = QPushButton('+', self)
        self.btn_equal = QPushButton('=', self)
        
        self.h_box.addWidget(self.line_edit)
        
        self.h1_box.addWidget(self.btn_num_1)
        self.h1_box.addWidget(self.btn_num_2)
        self.h1_box.addWidget(self.btn_num_3)
        self.h1_box.addWidget(self.btn_slash)
        
        self.h2_box.addWidget(self.btn_num_4)
        self.h2_box.addWidget(self.btn_num_5)
        self.h2_box.addWidget(self.btn_num_6)
        self.h2_box.addWidget(self.btn_star)
        
        self.h3_box.addWidget(self.btn_num_7)
        self.h3_box.addWidget(self.btn_num_8)
        self.h3_box.addWidget(self.btn_num_9)
        self.h3_box.addWidget(self.btn_minus)
        
        self.h4_box.addWidget(self.btn_num_0)
        self.h4_box.addWidget(self.btn_equal)
        self.h4_box.addWidget(self.btn_plus)
        
        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.h1_box)
        self.v_box.addLayout(self.h2_box)
        self.v_box.addLayout(self.h3_box)
        self.v_box.addLayout(self.h4_box)
        
        self.setLayout(self.v_box)
        
        self.show()

app = QApplication([])
calc = Window()
app.exec_()