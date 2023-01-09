from os import environ
from typing import Final


class Keys:
    BOT_TOKEN: Final = environ.get('BOT_TOKEN', 'Define a token in a virtual environment!')
