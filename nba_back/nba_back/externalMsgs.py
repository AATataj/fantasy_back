import json
from channels.generic.websocket import WebsocketConsumer

def testingExternal(websocket):
    message  = "external message!!"
    self.send(text_data=json.dumps({
        'message': message
    }))