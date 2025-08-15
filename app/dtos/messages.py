from datetime import datetime
from pydantic import BaseModel


class ChatListItemDTO(BaseModel):
    chat_oid: str
    title: str
    created_at: datetime


class ChatListenerDTO(BaseModel):
    oid: str