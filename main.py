
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from handlers.commands import (start, help, about, info, tokens, jokes, contacts)
from handlers.messages import (handle_message, handle_document, handle_sticker, handle_photo, handle_audio, handle_video)
from handlers.callback import get_callbacks
from handlers.error import handle_error
from config import BOT_TOKEN, logger

def main():
    if token := BOT_TOKEN:
        app = ApplicationBuilder().token(token).build()
        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('help', help))
        app.add_handler(CommandHandler('about', about))
        app.add_handler(CommandHandler('contacts', contacts))
        app.add_handler(CommandHandler('info', info))
        app.add_handler(CommandHandler('tokens', tokens))
        app.add_handler(CommandHandler("jokes", jokes))

        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
        app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
        app.add_handler(MessageHandler(filters.Sticker.ALL, handle_sticker))
        app.add_handler(MessageHandler(filters.VIDEO | filters.VIDEO_NOTE, handle_video))
        app.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, handle_audio))

        app.add_handler(CallbackQueryHandler(get_callbacks))

        app.add_error_handler(handle_error)
        logger.info('Starting...')
        app.run_polling()
    else:
        logger.error('BOT_TOKEN is None')
    



if __name__ == '__main__':
    main()



            







       




    









