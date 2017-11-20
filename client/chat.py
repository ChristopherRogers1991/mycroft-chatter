from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from collections import deque
from threading import Thread
from uuid import uuid1
import json
import sys
import websocket

from client.ui.generated.chat import Ui_ChatMainWindow

class ChatApplication(QtWidgets.QApplication):

    message_received = pyqtSignal(str, str)

    def __init__(self, args):
        super(ChatApplication, self).__init__(args)

        self.context = {'app-id': str(uuid1())}

        self.messages = deque(maxlen=100)

        self.ws = websocket.WebSocketApp("ws://localhost:8181/core",
                                    on_message=self.on_message)

        self.window = Ui_ChatMainWindow()
        self.window.setupUi(self.window)
        self.window.sendButton.clicked.connect(self.send_message)
        self.window.show()

    def connect_signal(self):
        self.message_received.connect(self.append_message)

    def append_message(self, sender, message):
        message = "{sender}: {message}".format(sender=sender, message=message)
        self.messages.append(message)
        self.window.chatHistory.setPlainText("\n".join(self.messages))

    def on_message(self, ws, message):
        data = json.loads(message)
        if data["type"] == "speak":
            message_text = data["data"]["utterance"]
            self.message_received.emit("Mycroft", message_text)

    def send_message(self):
        message = self.window.messageLineEdit.text()
        payload = json.dumps({
            "type": "recognizer_loop:utterance",
            "context" : self.context,
            "data": {
                "utterances": [message]
            }
        })
        self.ws.send(payload)
        self.message_received.emit("Me", message)
        self.window.messageLineEdit.clear()

if __name__ == "__main__":
    app = ChatApplication(sys.argv)
    app.connect_signal()
    websocket_thread = Thread(target=app.ws.run_forever)
    websocket_thread.start()
    sys.exit(app.exec_())
