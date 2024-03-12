from PyQt6.QtCore import QThread, pyqtSignal
import time

class TimerThread(QThread):
    time_left_signal = pyqtSignal(int)  # Сигнал для оновлення залишку часу
    finished_signal = pyqtSignal()  # Сигнал про завершення таймера

    def __init__(self, minutes):
        super().__init__()
        self.minutes = minutes
        self._is_running = True
        self.seconds_left = 0

    def run(self):
        self.seconds_left = self.minutes * 60
        while self._is_running and self.seconds_left > 0:
            time.sleep(1)
            self.seconds_left -= 1
            self.time_left_signal.emit(self.seconds_left)
        if self._is_running:
            self.finished_signal.emit()

    def stop(self):
        self._is_running = False
        self.wait()

    def get_time_left(self):
        return self.seconds_left
