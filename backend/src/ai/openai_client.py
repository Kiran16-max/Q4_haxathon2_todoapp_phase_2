# backend/src/ai/openai_client.py
import openai
import os
from typing import Dict, Any

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIClient:
    def __init__(self):
        self.client = openai.OpenAI(api_key=openai.api_key)
    
    def generate_response(self, prompt: str, conversation_history: list = None) -> str:
        """
        Generate a response from the OpenAI API based on the prompt and conversation history.
        """
        try:
            # Prepare messages for the API
            messages = [{"role": "system", "content": "You are a helpful assistant for managing tasks. You can help users add, list, update, and complete tasks. Respond in a friendly and concise manner."}]
            
            # Add conversation history if provided
            if conversation_history:
                messages.extend(conversation_history)
            
            # Add the current user message
            messages.append({"role": "user", "content": prompt})
            
            # Call the OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            # Extract and return the response
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            print(f"Error calling OpenAI API: {str(e)}")
            return "Sorry, I'm having trouble processing your request right now. Please try again later."

# Create a singleton instance
openai_client = OpenAIClient()

def get_openai_client():
    return openai_client