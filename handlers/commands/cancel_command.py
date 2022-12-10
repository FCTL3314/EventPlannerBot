import aiogram
import utils
import states

from data.config import BOT_ADMIN_IDS


async def cancel_command(message: aiogram.types.Message, state: aiogram.dispatcher.FSMContext):
    if message.from_user.id in BOT_ADMIN_IDS:
        await message.answer(text='✅*Создание события остановлено.*',
                             parse_mode='Markdown',
                             reply_markup=aiogram.types.reply_keyboard.ReplyKeyboardRemove())
        await state.finish()


def register_cancel_command_handlers(dp: aiogram.Dispatcher):
    dp.register_message_handler(callback=utils.misc.send_message.send_unable_execute_stop_command_message,
                                commands=['cancel'])
    dp.register_message_handler(callback=cancel_command, commands=['cancel'],
                                state=[states.create_event_states.CreateEventStates.get_event_name,
                                       states.create_event_states.CreateEventStates.get_event_description,
                                       states.create_event_states.CreateEventStates.get_event_picture,
                                       states.create_event_states.CreateEventStates.select_channel,
                                       states.create_event_states.CreateEventStates.send_event])
