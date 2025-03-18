from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 400)
        
        self.layout = QVBoxLayout()
        self.display = QLineEdit()
        self.layout.addWidget(self.display)
        
        self.grid_layout = QGridLayout()
        self.botoes = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 4)
        ]
        
        for btn_text, row, col, *span in self.botoes:
            button = QPushButton(btn_text)
            button.clicked.connect(lambda checked, text=btn_text: self.on_button_click(text))
            if span:
                self.grid_layout.addWidget(button, row, col, *span)
            else:
                self.grid_layout.addWidget(button, row, col)
        
        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)
        
    def on_button_click(self, text):
        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                resultado = eval(self.display.text())
                self.display.setText(str(resultado))
            except Exception:
                self.display.setText("Erro")
        else:
            self.display.setText(self.display.text() + text)

if __name__ == "__main__":
    app = QApplication([])
    window = Calculadora()
    window.show()
    app.exec()