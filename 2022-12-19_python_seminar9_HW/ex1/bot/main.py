import logging

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot.handlers import command_start, command_help
from bot.misc import Keys
from bot.misc import unknown_command, delete_abc

# Enable logging.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start_bot() -> None:
    """Run the bot."""
    # Create the Application and pass your bot token from the virtual environment to it.
    application = Application.builder().token(Keys.BOT_TOKEN).build()

    # Register the commands.
    application.add_handler(CommandHandler('start', command_start))
    application.add_handler(CommandHandler('help', command_help))
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))
    application.add_handler(MessageHandler(filters.TEXT, delete_abc))

    # Run the bot until it stops forcibly.
    application.run_polling()
