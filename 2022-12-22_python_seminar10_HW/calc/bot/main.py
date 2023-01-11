import logging

from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from bot.handlers import start, button
from bot.misc import Keys, unknown_command, get_calc

# Enable logging for console output.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start_bot() -> None:
    """Run the bot."""
    # Create the Application and pass your bot token from the virtual environment to it.
    application = Application.builder().token(Keys.BOT_TOKEN).build()

    # Register the commands.
    application.add_handler(CommandHandler(['start', 'help'], start))
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))
    application.add_handler(MessageHandler(filters.TEXT, get_calc))
    application.add_handler(CallbackQueryHandler(button))

    # Run the bot until it stops forcibly.
    application.run_polling()
