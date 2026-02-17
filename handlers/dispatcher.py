from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = "7688739624:AAGZrjz7dta_BEA-jSzpfmSkNO5O4Z8Yd_M"

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)
