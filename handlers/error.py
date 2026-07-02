
from telegram import Update
from telegram.ext import ContextTypes

from config import logger

async def handle_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error('Error', exc_info=context.error)

    if isinstance(update, Update) and update.message:
        try:
            await update.message.reply_text('You have error')
        except Exception as error:
            logger.error('Error with reply message - {}'.format(error))