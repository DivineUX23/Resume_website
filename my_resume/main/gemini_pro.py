
import google.generativeai as genai
import os
from .models import Conversation
from dotenv import load_dotenv
from decouple import config
import json
from django.core.exceptions import ValidationError
import markdown
from .models import Resume_info
from asgiref.sync import sync_to_async


gemini_api_key = config("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)



class Assistant():

    def __init__(self):

        #self.content = None
        #self.assistant = None

        self.system_instruction = None
        self.model = None
        self.convo = None

    async def initialize(self, content):
        #self.content = content

        self.generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
        }

        self.system_instruction = f"You're Divine's Assistant and your name is Jervis, You answer questions about Divine based on Following information: {content}"

        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                    generation_config=self.generation_config,
                                    system_instruction=self.system_instruction)

        self.convo = self.model.start_chat(history=[])


    async def generate_text(self, user_id, prompt: str):
        response = self.convo.send_message(prompt)

        try:
            conversation, created = await sync_to_async(Conversation.objects.get_or_create, thread_sensitive=True)(
                user_id=user_id, 
                defaults={'chat_history': {'conversation': []}})
            
            # Load the existing conversation history
            if conversation.chat_history:
                #conversation_data = conversation.chat_history
                conversation_history = conversation.chat_history.get('conversation', [])
            else:
                conversation_history = []
                
        except (TypeError, ValueError) as e:
            raise ValidationError(f"Error loading chat history: {e}")

        # Append the user's message to the conversation history
        conversation_history.append({
            'role': 'customer',
            'message': prompt
        })

        conversation_history.append({
            'role': 'agent',
            'message': markdown.markdown(response.text)
        })

        conversation_json = {'conversation': conversation_history}

        conversation.chat_history = conversation_json
        await sync_to_async(conversation.save)()

        # Print history and response for debugging purposes
        #print(conversation_json)
        #print(response.text)
        

        return markdown.markdown(response.text) if response.text else "Error processing response, try again later"