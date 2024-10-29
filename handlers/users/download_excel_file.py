from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.companies_keyboards import all_companies_default_keyboard
from keyboards.default.go_to_registration import go_registration_default_keyboard
from keyboards.default.menu_keyboards import back_to_menu
from loader import dp, db, bot


@dp.message_handler(text="📥 Excel fayl yuklab olish", state="*")
async def start_getting_company_id(message: types.Message, state: FSMContext):
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
    if user_role != "admin":
        await message.answer(text="🚫 Sizda botdan foydalanish uchun ruxsat mavjud emas", reply_markup=back_to_menu)
        return
    markup = await all_companies_default_keyboard()
    await message.answer(text="🏢 Hisobotni yuklab olish uchun Kompaniyani tanlang",
                         reply_markup=markup)
