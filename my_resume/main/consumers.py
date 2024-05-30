import json
import uuid
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from .gemini_pro import Assistant
from .models import Resume_info
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assistant = Assistant()
    
    async def connect(self):
        self.user_id = str(uuid.uuid4())
        
        content = await sync_to_async(Resume_info.objects.first)()

        print(content)

        await self.assistant.initialize(content)

        await self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'connected Succefully',
            'user_id': self.user_id
        }))

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        print('Message:', message)

        if message:
            response = await self.assistant.generate_text(self.user_id, message)
            print(f"this is the {response}")

            await self.send(text_data=json.dumps({
                'type': 'chat_message',
                'message': response
            }))