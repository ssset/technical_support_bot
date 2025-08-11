from functools import lru_cache
import environ

from pydantic_settings import BaseSettings

env = environ.Env()
environ.Env.read_env('.env')


class ProjectSettings(BaseSettings):
    TG_BOT_TOKEN: str = env('TG_BOT_TOKEN')
    GREETING_TEXT: str = env(
        'GREETENG_TEXT',
        default=(
            '''
                Добро пожаловать в бот технической поддержки.\n
                Пожалуйста, выберите чат для работы с клиентом.\n
                Получить список всех чатов: /chats. \n Выбрать чат: /set-chats
            '''
        )
    )
    WEB_API_BASE_URL: str = env('WEB_API_BASE_URL', default='http://localhost:8000')

@lru_cache(1)
def get_settings() -> ProjectSettings:
    return ProjectSettings()