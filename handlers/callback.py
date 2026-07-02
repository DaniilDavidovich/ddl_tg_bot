
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from services.jokes import load_data_from_url
from services.tokens import secret_did_handle, SecretType

from config import ADMIN_USERNAME


async def get_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    if query is None:
        return 
    
    await query.answer()

    if query.data == 'get_admin_username':
        await query.edit_message_text(text=f'Admin username: - @{ADMIN_USERNAME}')
    elif query.data == "jokes":
        next_button = [[InlineKeyboardButton("Next", callback_data="jokes")]]
        text = await load_data_from_url()

        if isinstance(text, str):
            await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(next_button))
            
    elif query.data == SecretType.free.value:
        await setup_logic(type=SecretType.free, query=query)
    elif query.data == SecretType.paid.value:
         await setup_logic(type=SecretType.paid, query=query)

    

async def setup_logic(type: SecretType, query):
    if type is not None:
        if text := secret_did_handle(type=type):
            next_button = get_next_button(type)
            await query.edit_message_text(text=text, reply_markup=next_button)


def get_next_button(type: SecretType) -> InlineKeyboardMarkup:
    next_button = [[InlineKeyboardButton("Next", callback_data=type.value)]]
    return InlineKeyboardMarkup(next_button)


