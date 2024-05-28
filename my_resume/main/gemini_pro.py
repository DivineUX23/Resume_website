
import google.generativeai as genai
import os
from .models import Conversation
from dotenv import load_dotenv
from decouple import config
import json
from django.core.exceptions import ValidationError
import markdown

#load_dotenv()
#gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_api_key = config("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

def read_content(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
        return content
    except FileNotFoundError as e:
        print(f"Error reading file: {e}")
        return ""
    except IOError as e:
        print(f"Error reading file: {e}")
        return ""



class Assistant():

  def __init__(self):

    self.content = read_content("main\Divine.txt")
      
    self.generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 0,
      "max_output_tokens": 8192,
      }

    self.system_instruction = f"You're Divine's Assistant and your name is Jervis, You answer questions about Divine based on Following information: {self.content}"

    self.model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                                  generation_config=self.generation_config,
                                  system_instruction=self.system_instruction)

    self.convo = self.model.start_chat(history=[])


  @staticmethod
  def read_content(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
        return content
    except FileNotFoundError as e:
        print(f"Error reading file: {e}")
        return ""
    except IOError as e:
        print(f"Error reading file: {e}")
        return ""



  def generate_text(self, user_id, prompt: str):
    response = self.convo.send_message(prompt)

    try:
        conversation, created = Conversation.objects.get_or_create(
            user_id=user_id, 
            defaults={'chat_history': {'conversation': []}})
            #jsonpickle.encode()
        
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
    conversation.save()

    # Print history and response for debugging purposes
    print(conversation_json)
    print(response.text)
    

    return markdown.markdown(response.text) if response.text else "Error processing response, try again later"