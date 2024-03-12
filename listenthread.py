from PyQt6.QtCore import QThread, pyqtSignal

class ListenThread(QThread):
    received_audio = pyqtSignal(object)
    finished = pyqtSignal()
    debug = pyqtSignal()
    def __init__(self, recognizer, mic,phrase_time_limit):
        super().__init__()
        self.recognizer = recognizer
        self.mic = mic
        self.is_running = False
        self.phrase_time_limit = phrase_time_limit
    def run(self):
        if not self.is_running:
            self.is_running = True
        while self.is_running:
            self.debug.emit()
            with self.mic as source:
                audio = self.recognizer.listen(source,phrase_time_limit=self.phrase_time_limit)
                self.received_audio.emit(audio)
        self.finished.emit()

    def stop(self):
        self.is_running = False
    
    def isListening(self):
        return self.is_running
    
    def setphrase_time_limit(self,time):
        self.phrase_time_limit = time
