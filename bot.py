from aiogram import Bot, Dispatcher, executor, types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer(
        "📉 Бот «Что подешевеет скоро»\n\n"
        "Пока это тестовая версия.\n"
        "Бот запущен и работает ✅"
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
