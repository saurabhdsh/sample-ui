# model_selector.py

import os
import openai

class ModelSelector:
    @staticmethod
    def select(model_name="openai"):
        """
        Selects and initializes the specified model.
        """
        if model_name.lower() == "openai":
            return OpenAIModel()
        elif model_name.lower() == "llama":
            return LlamaModel()
        else:
            raise ValueError(f"Model '{model_name}' is not supported. Available options: 'openai', 'llama'.")

class OpenAIModel:
    def __init__(self):
        """
        Initializes the OpenAI model by setting the API key from environment variable.
        """
        if not os.getenv("OPENAI_API_KEY"):
            raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_response(self, prompt):
        """
        Uses OpenAI API to generate a response based on the prompt.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a medical assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"Error generating response with OpenAI: {str(e)}")
            return None

class LlamaModel:
    def __init__(self):
        """
        Initializes the Llama model (assuming you have some setup for it).
        """
        pass

    def generate_response(self, prompt):
        """
        Generate a response using the Llama model (assuming Llama API integration or local execution).
        """
        return f"Llama model response for the prompt: {prompt}"
