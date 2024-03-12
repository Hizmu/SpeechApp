from PyQt6.QtWidgets import QVBoxLayout, QLabel, QDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class CommandsInfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Інформація про команди")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        info_text = """Команди, які ви можете використовувати:
- "запуск таймера на X хвилин" для запуску таймера на X хвилин
- "почати запис оцінок групи [назва групи]" для створення файлу оцінок
- "запиши оцінку [ім'я] [оцінка]" для запису оцінки студенту
- "відкрий ексель файл" 
- "відкрий файл [назва файлу]" для відкриття файлу
- "скільки часу залишилося" для перевірки часу, що залишився на таймері
- "зупинити таймер" зупиняє таймер"""

        label = QLabel(info_text)
        label.setFont(QFont('Arial', 12))
        layout.addWidget(label)
        
        self.setLayout(layout)
        self.adjustSize()