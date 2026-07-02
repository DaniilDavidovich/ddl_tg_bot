
import os

from telegram import Update
from telegram.ext import ContextTypes

from handlers.commands import (contacts, help, start, info, tokens, jokes, about)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if message and message.text:
        if message.text == 'Contacts':
            await contacts(update=update, context=context)
        elif message.text == 'Help':
            await help(update=update, context=context)
        elif message.text == 'Start':
            await start(update=update, context=context)
        elif message.text == 'About':
            await about(update=update, context=context)
        elif message.text == 'Info':
            await info(update=update, context=context)
        elif message.text == 'Tokens':
            await tokens(update=update, context=context)
        elif message.text == 'Jokes':
            await jokes(update=update, context=context)
        else:
            if context.user_data:
                count = context.user_data.get('messages_count', 0) + 1
                context.user_data['messages_count'] = count

            await message.reply_text('Choose button')


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if message:
        if context.user_data:
            count = context.user_data.get('image_count', 0) + 1
            context.user_data['image_count'] = count
        await message.reply_text('Thanks for image')


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if not message:
        return
    
    document = message.document

    if not document:
        await message.reply_text("No document attached.")
        return

    file_name = document.file_name
    if file_name and file_name.endswith('.txt'):
        file = await document.get_file() 
        if file:
            file_path = await file.download_to_drive()
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    await message.reply_text(f'Text from file:\n{content[:4096]}')

                    if context.user_data:
                        count = context.user_data.get('documents_count', 0) + 1
                        context.user_data['documents_count'] = count
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)
        else:
            await message.reply_text("Could not retrieve file.")
    else:
        await message.reply_text('This is not a .txt file (or file has no name).')

    


async def handle_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if message:

        if context.user_data:
            count = context.user_data.get('stickers_count', 0) + 1
            context.user_data['stickers_count'] = count

        await message.reply_text('Thanks for sticker')


async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if message:

        if context.user_data:
            count = context.user_data.get('video_count', 0) + 1
            context.user_data['video_count'] = count

        await message.reply_text('Thanks for video')


async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if message:

        if context.user_data:
            count = context.user_data.get('audio_count', 0) + 1
            context.user_data['audio_count'] = count

        await message.reply_text('Thanks for audio')
