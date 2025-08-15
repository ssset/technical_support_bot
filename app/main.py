import asyncio

from aiogram import Bot, Dispatcher
from bot.handlers.commands import router as command_router
from settings import get_settings

async def main():
    settings = get_settings()
    
    bot = Bot(token=settings.TG_BOT_TOKEN)

    dp = Dispatcher()

    dp.include_routers(
        command_router,
    )

    try:
        await dp.start_polling(bot)
    finally:
        bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())