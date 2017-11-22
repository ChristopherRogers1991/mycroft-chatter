from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from collections import deque
from threading import Thread
import json
import sys
import time
import websocket

from client.ui.generated.chat import Ui_ChatMainWindow

class ChatApplication(QtWidgets.QApplication):

    message_received = pyqtSignal(str, str)

    def __init__(self, args):
        super(ChatApplication, self).__init__(args)

        self.messages = deque(maxlen=100)

        self.ws = self.create_websocket()
        self.connected = False
        self.window = Ui_ChatMainWindow()
        self.window.setupUi(self.window)
        self.window.sendButton.clicked.connect(self.send_message)
        self.window.show()

    def create_websocket(self):
        return websocket.WebSocketApp("ws://localhost:8181/core",
                                      on_message=self.on_message,
                                      on_error=self.on_error,
                                      on_close=self.on_close,
                                      on_open=self.on_open)


    def connect_signal(self):
        self.message_received.connect(self.append_message)

    def append_message(self, sender, message):
        message = "{sender}: {message}".format(sender=sender, message=message)
        self.messages.append(message)
        self.window.chatHistory.setPlainText("\n".join(self.messages))
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        scroll_bar = self.window.chatHistory.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())

    def on_message(self, ws, message):
        data = json.loads(message)
        if data["type"] == "speak":
            message_text = data["data"]["utterance"]
            self.message_received.emit("Mycroft", message_text)

    def on_open(self, ws):
        self.message_received.emit("System", "Connection established!")
        self.connected = True

    def on_close(self, ws):
        self.connected = False

    def on_error(self, ws, error):
        self.connected = False
        try:
            self.ws.close()
            self.message_received\
                .emit("ERROR","Cannot connect to Mycroft! Retrying...")
        except Exception as e:
            pass
        time.sleep(2)
        self.ws = self.create_websocket()
        self.start_websocket()

    def start_websocket(self):
        websocket_thread = Thread(target=app.ws.run_forever)
        websocket_thread.start()

    def send_message(self):
        if not self.connected:
            return
        message = self.window.messageLineEdit.text()
        payload = json.dumps({
            "type": "recognizer_loop:utterance",
            "context" : None,
            "data": {
                "utterances": [message]
            }
        })
        self.ws.send(payload)
        self.message_received.emit("Me", message)
        self.window.messageLineEdit.clear()

if __name__ == "__main__":
    app = ChatApplication(sys.argv)
    app.start_websocket()
    app.connect_signal()
    app.exec_()
    app.ws.close()
