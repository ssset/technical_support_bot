from dataclasses import dataclass

from exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class ChatListRequestException(ApplicationException):
    status_code: int
    response_content: str
    
    @property
    def message(self):
        return 'Не удалось получить список всех чатов.'
    

@dataclass(frozen=True, eq=False)
class ChatListenersRequestException(ApplicationException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return f'Не удалось получить список всех слушателей чата. Ошибка {self.status_code}, контент: {self.response_content}'
