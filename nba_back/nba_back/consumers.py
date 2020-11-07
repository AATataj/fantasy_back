# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer

class ProgressConsumer(WebsocketConsumer):
    def connect(self):
        print("do we ever get into the connect function?")
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message
        }))