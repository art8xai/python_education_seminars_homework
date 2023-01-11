from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Callback data
ONE, TWO, THREE = range(3)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send message on '/start'."""
    # Build InlineKeyboard where each button has a displayed text and a string as callback_data.
    # The keyboard is a list of button rows, where each row is in turn a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton('How to use? 🤔', callback_data=str(ONE)),
            InlineKeyboardButton('Example 🤓', callback_data=str(TWO)),
            InlineKeyboardButton('Continue 😎', callback_data=str(THREE))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text(text='I can help you solve an arithmetic expression. Please choose:',
                                    reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and sends the message text."""
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed.
    await query.answer()
    if query.data == str(ONE):
        await query.message.reply_html(
            text='To calculate the value of an arithmetic expression, enter it in the message.\n\n<b>For action signs, '
                 'use:</b>\n<b>+</b>   for addition;\n<b>-</b>   for subtraction;\n<b>*</b>   for multiplication;\n'
                 '<b>/</b>   for division;\n<b>^</b>   for exponentiation.\n\nSeparate the fractional part with a dot.'
                 '\nIf the expression contains parentheses, make sure that the number of opening and closing'
                 'parentheses is the same.'
        )
    elif query.data == str(TWO):
        await query.message.reply_text(text='Example:\n((1 + 2 * 3)^2 - (5 + 6) * 7) / 8 + 9.9')
    else:
        await query.message.reply_text(text='Enter an arithmetic expression:')
