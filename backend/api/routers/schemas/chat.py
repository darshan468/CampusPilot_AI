from pydantic import BaseModel


class ChatRequest(BaseModel):

    query: str

    memory: dict = {}