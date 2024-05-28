import json
import uuid
from channels.generic.websocket import WebsocketConsumer
from .gemini_pro import Assistant

class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assistant = Assistant()
    
    def connect(self):
        self.user_id = str(uuid.uuid4())
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'connected Succefully',
            'user_id': self.user_id
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        print('Message:', message)

        if message:
            response = self.assistant.generate_text(self.user_id, message)
            print(f"this is the {response}")

            self.send(text_data=json.dumps({
                'type': 'chat_message',
                'message': response
            }))