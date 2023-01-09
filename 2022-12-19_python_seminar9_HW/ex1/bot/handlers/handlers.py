from telegram import Update
from telegram.ext import ContextTypes


async def command_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('I can help you remove all words containing the phrase "abc", for this send '
                                    'a message with the text.')


async def command_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text('I can help you remove all words containing the phrase "abc", for this send '
                                    'a message with the text.')
