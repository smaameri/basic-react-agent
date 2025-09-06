from anthropic import Anthropic
from typing import List, Dict
from dotenv import load_dotenv
from anthropic.types import Message

import os

load_dotenv()


class ClaudeClient:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    def send_messages_with_tools(
            self,
            messages: List[Dict[str, str]],
            tools
    ) -> Message:
        try:
            print(messages)
            return self.client.messages.create(
                max_tokens=1028,
                model="claude-opus-4-20250514",
                system=self.system_prompt,
                messages=messages,
                tools=tools,
            )
        except Exception as e:
            raise Exception(f"Failed to create message: {str(e)}")
