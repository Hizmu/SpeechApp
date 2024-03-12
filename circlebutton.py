from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QPainter, QBrush, QPen, QFont
from PyQt6.QtCore import Qt, QRect

class CircleButton(QPushButton):
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.state = "waiting"  # Стани: "waiting", "listening", "processing"
        self.updateText()
        self.setStyleSheet("QWidget {border: none;}")
        self.colorText = Qt.GlobalColor.black
        self.texts = {
            "waiting": "Натиснути і тримати",
            "listening": "Слухаю...",
            "processing": "Обробляю...",
        }
        self.colors = {
            "waiting": Qt.GlobalColor.lightGray,
            "listening": Qt.GlobalColor.red,
            "processing": Qt.GlobalColor.yellow,
        }
        self.colorTexts = {
            "waiting": Qt.GlobalColor.black,
            "listening": Qt.GlobalColor.white,
            "processing": Qt.GlobalColor.black,
        }
        
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)
        qp.setPen(QPen(Qt.PenStyle.NoPen))
        
        qp.setBrush(QBrush(self.colors[self.state]))

        size = min(self.width(), self.height())  
        qp.drawEllipse((self.width() - size) // 2, (self.height() - size) // 2, size, size)

        qp.setPen(QPen(self.colorTexts[self.state]))
        qp.setFont(QFont('Arial', size // 15)) 
        rect = QRect(0, 0, self.width(), self.height())
        qp.drawText(rect, Qt.AlignmentFlag.AlignCenter, self.text)

    def updateText(self, text="Натиснути і тримати"):
        self.text = text
        self.update() 

    def setState(self, newState):
        self.state = newState
        if self.state == "waiting":
            self.setEnabled(True)
            
            self.updateText(self.texts["waiting"])
        elif self.state == "listening":
            self.updateText(self.texts["listening"])
        elif self.state == "processing":
            self.setEnabled(False)
            self.updateText(self.texts["processing"])
        else:
            self.setEnabled(True)
            self.updateText("Unknown State")

    def enterEvent(self, event):
        self.setCursor(Qt.CursorShape.PointingHandCursor)  # Змінюємо курсор
        super().enterEvent(event)
        
    def setColors(self, waiting=None, listening=None, processing=None, text=None):
        if waiting:
            self.colors["waiting"] = waiting
        if listening:
            self.colors["listening"] = listening
        if processing:
            self.colors["processing"] = processing
        if text:
            self.colors["text"] = text
        self.update()
    def setColorTexts(self, waiting=None, listening=None, processing=None, text=None):
        if waiting:
            self.colorTexts["waiting"] = waiting
        if listening:
            self.colorTexts["listening"] = listening
        if processing:
            self.colorTexts["processing"] = processing
        self.update()