from .callback_game import CallbackGame
from .callback_query import CallbackQuery
from .force_reply import ForceReply
from .game_high_score import GameHighScore
from .inline_keyboard_button import InlineKeyboardButton
from .inline_keyboard_markup import InlineKeyboardMarkup
from .keyboard_button import KeyboardButton
from .reply_keyboard_markup import ReplyKeyboardMarkup
from .reply_keyboard_remove import ReplyKeyboardRemove

# added
from .bot_info import BotInfo
from .bot_command import BotCommand

__all__ = [
    "CallbackGame", "CallbackQuery", "ForceReply", "GameHighScore", "InlineKeyboardButton", "InlineKeyboardMarkup",
    "KeyboardButton", "ReplyKeyboardMarkup", "ReplyKeyboardRemove",

    # added
    "BotInfo",
    "BotCommand"
]
