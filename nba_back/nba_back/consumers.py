import json, sys
from channels.generic.websocket import WebsocketConsumer
import mysql.connector

from .externalMsgs import testingExternal
sys.path.insert(1, sys.path[0]+'/../../fantasy_bot')
from fantasyAI import rotoworldScraper, liveBoxScrape # scraper for play-by-plays to be added

class ProgressRoto(WebsocketConsumer):
    def connect(self):
        self.accept()        
        cnx = mysql.connector.connect(user="slick", password = "muresan44", host ='127.0.0.1', database='nba')
        rotoworldScraper.updateRoto(cnx, self)
        self.send(text_data=json.dumps({
        'progress': 100
        }))
        self.close()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        "this is in case we want to recieve more data from the front end"
class ProgressBox(WebsocketConsumer):
    def connect(self):
        self.accept()
        cnx = mysql.connector.connect(user="slick", password = "muresan44", host ='127.0.0.1', database='nba')
        liveBoxScrape.scrapeScores(cnx, self)
        self.send(text_data=json.dumps({
        'progress': 100
        }))
        self.close()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        "this is in case we want to recieve more data from the front end" 
class ProgressPlay(WebsocketConsumer):
    """
    We'll flesh this out after we get a scraper for play by plays
    """
    # def connect(self):
    #     self.accept()
    #     cnx = mysql.connector.connect(user="slick", password = "muresan44", host ='127.0.0.1', database='nba')
    #     liveBoxScrape.scrapeScores(cnx, self)
    #     self.send(text_data=json.dumps({
    #     'progress': 100
    #     }))
    #     self.close()

    # def disconnect(self, close_code):
    #     pass

    # def receive(self, text_data):
    #     "this is in case we want to recieve more data from the front end" 