
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from config import logger
from keyboards.reply import reply_markup
from services.tokens import SecretType
from services.jokes import load_data_from_url 

from config import ADMIN_USERNAME


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if update.message and (user := update.effective_user):
        name = user.first_name or "Guest"
      
        await update.message.reply_text(f'Hello, {name}', reply_markup=reply_markup)

        if context.user_data is not None:
            if 'username' not in context.user_data:
                context.user_data['username'] = user.username or "Unknown"
            if 'first_name' not in context.user_data:
                context.user_data['first_name'] = user.first_name or "Unknown"
            if 'last_name' not in context.user_data:
                context.user_data['last_name'] = user.last_name or "Unknown"
            if 'id' not in context.user_data:
                context.user_data['id'] = user.id or "Unknown"
            if 'is_premium' not in context.user_data:
                context.user_data['is_premium'] = user.is_premium or False
            if 'language_code' not in context.user_data:
                context.user_data['language_code'] = user.language_code or 'Unknown'
            if 'is_bot' not in context.user_data:
                context.user_data['is_bot'] = user.is_bot or False
            

            username = context.user_data.get('username', 'Unknown')
            logger.info('Start work with user @{}'.format(username))
    


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
f'''Commands:
/start - start bot
/about - get info
/help - get help
/contacts - get admin username
/info - get info about you 
/tokens - get actual tokens
/jokes - get joke from Chuck Norris
''')


async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(f'Admin contact - @{ADMIN_USERNAME}')


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    buttons = [
        [
            InlineKeyboardButton(text='Admin', url=f'https://t.me/{ADMIN_USERNAME}'),
            InlineKeyboardButton(text='Get admin username', callback_data='get_admin_username'),
        ]
    ]

    if update.message:
        await update.message.reply_text(f'You did choose about', reply_markup=InlineKeyboardMarkup(buttons))

    
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data:
        first_name = context.user_data.get('first_name', "Unknown")
        last_name = context.user_data.get('last_name', "Unknown")
        id = context.user_data.get('id', "Unknown")
        is_premium = context.user_data.get('is_premium', False)
        language_code = context.user_data.get('language_code', "Unknown")
        is_bot = context.user_data.get('is_bot', False)
        username = context.user_data.get('username', "Unknown")

        audio_count = context.user_data.get('audio_count', 0)
        video_count = context.user_data.get('video_count', 0)
        image_count = context.user_data.get('image_count', 0)
        messages_count = context.user_data.get('messages_count', 0)
        stickers_count = context.user_data.get('stickers_count', 0)
        documents_count = context.user_data.get('documents_count', 0)

        if update.message:
            await update.message.reply_text(
f'''
Bot saved about you:
Username - @{username}
First Name - {first_name}
Last Name - {last_name}
ID - {id}
Is Premium - {is_premium}
Language Code - {language_code}
Is Bot - {is_bot}
                                        
Content: 
Audios - {audio_count}
Videos - {video_count}
Images - {image_count}
Messages - {messages_count}
Stickers - {stickers_count}
Documents - {documents_count}
''')



async def tokens(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    buttons = [
        [
            InlineKeyboardButton('Secret Key 1', callback_data=SecretType.free.value)
        ],
        [
            InlineKeyboardButton('Secret Key 2', callback_data=SecretType.paid.value)
        ],
    ]

    if update.message:
        await update.message.reply_text('Choose Token what you want', reply_markup=InlineKeyboardMarkup(buttons))



async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = await load_data_from_url()
    next_button = [
        [
            InlineKeyboardButton('Next', callback_data="jokes")
        ]
    ]

    if update.message :
        if isinstance(text, str):
            await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(next_button))



    