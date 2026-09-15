import datetime
from langchain_core.tools import tool
from zoneinfo import ZoneInfo


# Tool 1: Get current date and time details
@tool
def get_current_date_and_time():
    """
    Get the current date and time in IST.
    Use this whenever the user asks what time or date it is.
    Returns:
        A string with the current date and time, e.g. '2026-09-15 14:30:30 IST'
    """
    now = datetime.datetime.now(ZoneInfo("Asia/Kolkata"))
    return now.strftime("%Y-%m-%d %H:%M:%S IST")
