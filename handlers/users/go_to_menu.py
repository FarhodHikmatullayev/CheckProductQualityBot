from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.go_to_registration import go_registration_default_keyboard
from keyboards.default.menu_keyboards import main_menu_default_keyboard, back_to_menu
from loader import dp, db, bot


@dp.message_handler(text='🔙 Bosh Menyu', state='*')
@dp.message_handler(text="🤖 Botdan foydalanish 🤖", state='*')
async def go_to_menu_function(message: types.Message, state: FSMContext):
    try:
        await state.finish()
    except:
        pass
    user_telegram_id = message.from_user.id
    users = await db.select_users(telegram_id=user_telegram_id)
    if not users:
        await message.answer(text="🚫 Sizda botdan foydalanish uchun ruxsat mavjud emas,\n"
                                  "📝 Botdan foydalanish uchun ro'yxatdan o'tishingiz kerak 👇",
                             reply_markup=go_registration_default_keyboard)
        return

    user = users[0]
    user_role = user['role']
    if user_role != 'admin':
        await message.answer(text="🚫 Sizda botdan foydalanish uchun ruxsat mavjud emas", reply_markup=back_to_menu)
        return

    await message.answer(text="Bo'limlardan birini tanlang 👇", reply_markup=main_menu_default_keyboard)
