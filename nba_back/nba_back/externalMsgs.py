import json
from channels.generic.websocket import WebsocketConsumer

def testingExternal(websocket):
    message  = "external message!!"
    print("the websocket details are : " + str(websocket))
    websocket.send(text_data=json.dumps({
        'progress': message
    }))
    return