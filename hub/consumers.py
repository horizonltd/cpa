from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from . import models
#from hub.models import Lecture

class LectureConsumer(WebsocketConsumer):

    #Method for connecting to the server for interacting live
    def connect(self):
        self.room_group_name = 'lectures'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    def receive(self, text_data):
        text_data_json = json.load(text_data)
        title = text_data_json['title']
        content = text_data_json['content']
        author =text_data_json['author']
        id  =text_data_json['id']

        #lecture = models.Lecture.objects.get(pk=id)
        lecture = models.Event.objects.get(pk=id)
        lecture.title = title
        lecture.content = content
        lecture.author = author
        lecture.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'add_lecture',
                'title': title,
                'content': content,
                'author': author,
                'id': id
            }
        )
    
    def add_lecture(self, event):
        title = event['title']
        content = event['content']
        author = event['author']
        id = event['id']

        self.send(text_data=json.dumps({
            'title': title,
            'content': content,
            'author': author,
            'id': id  
        }))
        

