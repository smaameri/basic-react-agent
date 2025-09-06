from abc import ABC

from pydantic import BaseModel
from app.context_window import ContextWindow, UserMessage, AssistantMessage, ToolUse, ToolResult, ToolUseMessage, \
    ToolResultMessage
from app.claude_client import ClaudeClient


class Tool(BaseModel):
    name: str
    description: str
    input_schema: object


system_prompt = """You are an AI assistant that takes Pizza Deliveries for the popular restaurant, Mamma's Pizzas.

Once you start chatting with a user, get their name, and check if they already exist in our system by using the get_user_information tool.

If they do not exist, make sure to get their address.

Ask what sort of pizza they would like to order. Once you have all the information you need, use the create_order tool to place the order.

Once placed, let the user know their order number and that their pizza will be delivered soon.
"""

tools = [
    Tool(
        name="get_user_information",
        description="Get users information from their name",
        input_schema={
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The users name"
                }
            },
            "required": ["name"]
        }
    ),
    Tool(
        name="create_order",
        description="Create a new order for a customer",
        input_schema={
            "type": "object",
            "properties": {
                "pizza_description": {
                    "type": "string",
                    "description": "A description of the pizza to order, including size and toppings"
                },
                "address": {
                    "type": "string",
                    "description": "The delivery address for the order"
                }
            },
            "required": ["pizza", "address"]
        }
    )
]


class AgentInterface(ABC):
    def act(self) -> str:
        pass


class PizzaAgent(AgentInterface):
    def __init__(
            self,
            context: ContextWindow,
            claude_client: ClaudeClient
    ):
        self.context = context
        self.claude_client = claude_client

    def send_message(self, user_message: str) -> str:
        self.context.add(UserMessage(content=user_message))
        response = self.act()
        self.context.add(AssistantMessage(content=response))
        return response

    def act(self) -> str:
        response = self.claude_client.send_messages_with_tools(
            messages=[msg.model_dump() for msg in self.context.conversation_history],
            tools=[tool.model_dump() for tool in tools]
        )

        print(response)

        if response.stop_reason == "tool_use":
            # Add tool use to context
            for content_block in response.content:
                if content_block.type == "tool_use":
                    # Add tool use message
                    tool_use = ToolUse(id="1", name=content_block.name, input=content_block.input)
                    self.context.add(ToolUseMessage(content=[tool_use]))

                    tool_result = self._execute_tool(tool_use.name, tool_use.input)

                    # Add tool result to context
                    tool_result_msg = ToolResult(tool_use_id="1", content=tool_result, is_error=False)
                    self.context.add(ToolResultMessage(content=[tool_result_msg]))

            # Make another API call to continue the conversation
            return self.act()

        return response.content[0].text if response.content else ""

    def _execute_tool(self, tool_name: str, tool_input: dict) -> str:
        if tool_name == "get_user_information":
            name = tool_input.get("name", "")
            return f"User {name} not found in system"
        elif tool_name == "create_order":
            pizza_description = tool_input.get("pizza_description", "")
            address = tool_input.get("address", "")
            order_id = "ORD12345"
            return f"Order {order_id} created for {pizza_description} to be delivered to {address}"
        else:
            return f"Unknown tool: {tool_name}"
