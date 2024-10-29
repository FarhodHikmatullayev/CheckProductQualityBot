from aiogram.dispatcher.filters.state import StatesGroup, State


class DownloadQualityState(StatesGroup):
    company_id = State()