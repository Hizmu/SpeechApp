from PyQt6.QtCore import pyqtSignal, QThread

class SpeechToText(QThread):
    result = pyqtSignal(str)
    error = pyqtSignal(Exception)

    def __init__(self, recognizer, audio, language="uk-UA"):
        super().__init__()
        self.recognizer = recognizer
        self.audio = audio
        self.language = language

    def run(self):
        try:
            text = self.recognizer.recognize_google(self.audio, language=self.language)
            self.result.emit(text)
        except Exception as e:
            self.error.emit(e)