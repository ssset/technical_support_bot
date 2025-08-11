from abc import ABC, abstractmethod
from dataclasses import dataclass
from urllib.parse import urljoin

from httpx import AsyncClient

from dtos.messages import ChatListItemDTO
from exceptions.chats import ChatListRequestException
from services.constans import CHAT_LIST_URL, DEFAULT_LIMIT, DEFAULT_OFFSET
from services.converters.chat import convert_chat_response_to_chat_dto

@dataclass
class BaseChatWebService(ABC):
    http_client: AsyncClient
    base_url: str

    @abstractmethod
    async def get_all_chats(self) -> list[ChatListItemDTO]:
        ...
    

@dataclass
class ChatWebService(BaseChatWebService):

    async def get_all_chats(self):
        response = await self.http_client.get(
            url=urljoin(base=self.base_url, url=CHAT_LIST_URL),
            params={'limit': DEFAULT_LIMIT, 'offset': DEFAULT_OFFSET}
        )
        if not response.is_success:
            raise ChatListRequestException(status_code=response.status_code, response_content=response.content.decode())
        
        json_data = response.json()
        
        return [convert_chat_response_to_chat_dto(chat_data=chat_data) for chat_data in json_data['items']]