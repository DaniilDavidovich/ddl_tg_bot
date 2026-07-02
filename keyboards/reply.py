
from telegram import ReplyKeyboardMarkup

reply_markup = ReplyKeyboardMarkup(
    [['Start'], ['Help', 'About', 'Contacts'], ['Info', 'Tokens','Jokes']],
    resize_keyboard=True,
    one_time_keyboard=False
)