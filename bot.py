from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import random
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

hugs = [
"🤗 {user} обнял(а) {target}!",
"❤️ {user} крепко обнял(а) {target}!",
"😊 {user} тепло обнял(а) {target}!"
]

kisses = [
"😘 {user} поцеловал(а) {target}!",
"💋 {user} подарил(а) поцелуй {target}!"
]

hits = [
"👊 {user} ударил(а) {target}!",
"💥 {target} получил(а) мощный удар от {user}!"
]

pats = [
"😊 {user} погладил(а) {target} по голове!",
"🤗 {user} заботливо погладил(а) {target}!"
]

def get_target(message):
args = message.text.split()
if len(args) < 2:
return None
return args[1]

@dp.message(Command("обнять"))
async def hug(message: types.Message):
target = get_target(message)
if not target:
await message.answer("Укажи кого обнять 😊")
return
await message.answer(random.choice(hugs).format(user=message.from_user.first_name, target=target))

@dp.message(Command("поцеловать"))
async def kiss(message: types.Message):
target = get_target(message)
if not target:
await message.answer("Укажи кого поцеловать 😘")
return
await message.answer(random.choice(kisses).format(user=message.from_user.first_name, target=target))

@dp.message(Command("ударить"))
async def hit(message: types.Message):
target = get_target(message)
if not target:
await message.answer("Укажи кого ударить 👊")
return
await message.answer(random.choice(hits).format(user=message.from_user.first_name, target=target))

@dp.message(Command("погладить"))
async def pat(message: types.Message):
target = get_target(message)
if not target:
await message.answer("Укажи кого погладить 😊")
return
await message.answer(random.choice(pats).format(user=message.from_user.first_name, target=target))

@dp.message(Command("монетка"))
async def coin(message: types.Message):
await message.answer(random.choice(["🪙 Орёл!", "🪙 Решка!"]))

@dp.message(Command("кубик"))
async def dice(message: types.Message):
await message.answer(f"🎲 Выпало: {random.randint(1, 6)}")

@dp.message(Command("шанс"))
async def chance(message: types.Message):
await message.answer(f"📊 Шанс: {random.randint(0, 100)}%")

@dp.message(Command("старт"))
async def start_cmd(message: types.Message):
await message.answer(
"👋 Привет!\n\n"
"Доступные команды:\n"
"/обнять @user\n"
"/поцеловать @user\n"
"/ударить @user\n"
"/погладить @user\n"
"/монетка\n"
"/кубик\n"
"/шанс"
)

async def main():
await dp.start_polling(bot)

if name == "main":
asyncio.run(main())