import datetime
import random
from langchain_core.tools import tool
from zoneinfo import ZoneInfo

# Constants
HEADS = "Heads"
TAILS = "Tails"


# Tool 1: Get current date and time details
@tool
def get_current_date_and_time() -> str:
    """
    Get the current date and time in IST.
    Use this whenever the user asks what time or date it is.
    :return:
        A string with the current date and time, e.g. '2026-09-15 14:30:30 IST'
    """
    now = datetime.datetime.now(ZoneInfo("Asia/Kolkata"))
    return now.strftime("%Y-%m-%d %H:%M:%S IST")

# Tool 2: Flip a coin
@tool
def flip_coin() -> str:
    """
    Flip a coin and get a random result of Heads or Tails.
    Use this whenever the user asks to flip a coin.
    :return:
        A string, either "Heads" or "Tails".
    """
    return random.choice([HEADS, TAILS])

# Tool 3: Roll a die of n sides
@tool
def roll_dice(n: int = 6) -> int:
    """
    Get a random roll of dice with n sides.
    Use this whenever the user asks to roll a dice.
    :param n: Sides of a die. Default is 6
    :return:
        A random number between 1 and n, inclusive.
    """
    return random.randint(1, n)
