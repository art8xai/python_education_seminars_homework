from telegram import Update
from telegram.ext import ContextTypes

from bot.misc.math import get_check_parentheses, get_expression_solution
from database import log_file


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when an unknown command is entered."""
    await update.message.reply_text("Sorry, I didn't understand that command.")


async def get_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Calculate the mathematical expression received in the message."""
    if get_check_parentheses(update.message.text):
        try:
            result = get_expression_solution(update.message.text)
        except IndexError:
            await update.message.reply_text('Sorry, there are not enough characters in the expression, '
                                            'please try again.', quote=True)
            log_file(update, update.message.text, 'error, not enough characters in the expression')
        except ValueError:
            await update.message.reply_text('Sorry, there are invalid characters in the expression, '
                                            'please try again.', quote=True)
            log_file(update, update.message.text, 'error, invalid characters in the expression')
        else:
            await update.message.reply_text(f'Result:\n{result}')
            log_file(update, update.message.text, result)
    else:
        await update.message.reply_text("Sorry, the number of parentheses doesn't match, please try again.",
                                        quote=True)
        log_file(update, update.message.text, "error, the number of parentheses doesn't match")
