from pydantic import BaseModel


class UserMessage(BaseModel):
    content: str
    role: str = "user"


class AssistantMessage(BaseModel):
    content: str
    role: str = "assistant"


class ToolUse(BaseModel):
    type: str = "tool_use"
    id: str
    name: str
    input: dict


class ToolUseMessage(BaseModel):
    role: str = "assistant"
    content: list[ToolUse]


class ToolResult(BaseModel):
    type: str = "tool_result"
    tool_use_id: str
    content: str
    is_error: bool


class ToolResultMessage(BaseModel):
    role: str = "user"
    content: list[ToolResult]


class ContextWindow(BaseModel):
    conversation_history: list

    def add(self, message: UserMessage | AssistantMessage | ToolUseMessage | ToolResultMessage):
        self.conversation_history.append(message)
