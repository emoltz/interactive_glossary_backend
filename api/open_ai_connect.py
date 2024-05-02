from openai import OpenAI
from openai import OpenAIError
from enum import Enum


class OpenAIModels(Enum):
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo"


client = OpenAI()


class OpenAIConnect():
    def __init__(self, system_prompt="", temperature=0.5, max_tokens=500, model="gpt-4-turbo", json_object=True,
                 json_format=None,
                 timeout=20):
        self.client = OpenAI()
        if not json_format:
            json_format = {"response": "your response here"}
        self.json_format = json_format

        if not system_prompt:
            system_prompt = f"""
            The following is a conversation with an AI assistant. 
            The assistant is helpful, creative, clever, and very friendly. 
            Please respond in json format: {self.json_format}
            """
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model = model
        self.json_object = json_object
        self.timeout = timeout

    def get_response(self, prompt: str, system_prompt: str = None) -> str or None:
        if not system_prompt:
            system_prompt = self.system_prompt

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                response_format={"type": "json_object"},
                timeout=self.timeout
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            raise ValueError("Error in OpenAIConnect.get_response: ", e)
