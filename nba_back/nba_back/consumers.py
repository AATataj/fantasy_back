import json, sys
from channels.generic.websocket import WebsocketConsumer
import mysql.connector

from .externalMsgs import testingExternal
sys.path.insert(1, sys.path[0]+'/../../')
#sys.path.insert(1, '/home/slick/Documents/fantasy_bot')
from fantasy_bot import rotoworldScraper


class ProgressConsumer(WebsocketConsumer):
    def connect(self):
        print("do we ever get into the connect function?")
        self.accept()
        message = "hellows"
        
        cnx = mysql.connector.connect(user="slick", password = "muresan44", host ='127.0.0.1', database='nba')

        rotoworldScraper.updateRoto(cnx)
        self.send(text_data=json.dumps({
            'progress': message
        }))


    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
        print ("message received")