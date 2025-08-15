from  aiogram import Router, types
from aiogram.filters import Command

from bot.handlers.converters.chats import convert_chats_dtos_to_message
from containers.factories import get_container
from services.web import BaseChatWebService
from settings import get_settings

router = Router(name='commands_router')

@router.message(Command('start'))
async def start_handler(message: types.Message):
    settings = get_settings()
    await message.answer(
        text=settings.GREETING_TEXT
    )


@router.message(Command('chats'))
async def get_all_chats_handler(message: types.Message):
    container = get_container()

    async with container() as request_container:
        service = await request_container.get(BaseChatWebService)
        chats = await service.get_all_chats()

        await message.answer(
            text=convert_chats_dtos_to_message(chats=chats),
            parse_mode='MarkdownV2'
        )