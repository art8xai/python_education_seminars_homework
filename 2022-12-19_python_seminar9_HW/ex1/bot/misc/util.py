from telegram import Update
from telegram.ext import ContextTypes


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when an unknown command is entered."""
    await update.message.reply_text("Sorry, I didn't understand that command.")


async def delete_abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Delete words containing the phrase "abc" in the message."""
    phrase = 'abc'
    text_source = update.message.text.split()
    result = ' '.join(filter(lambda x: phrase not in x.lower(), text_source))
    if result == '':
        await update.message.reply_text('Hmm, I removed all the words, so there is nothing to return.', quote=True)
    else:
        await update.message.reply_text(result)
