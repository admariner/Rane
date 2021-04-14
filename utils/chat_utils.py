from utils.utils import get_session
from utils import utils


def autocolor(testing: bool = False) -> str:
    """Insert role color into a user's username."""
    # TODO room specific autocolor
    session = get_session()

    if testing:
        session = {"username": "Jush"}

    data = {
        "table": "admins",
        "filename": "admins",
        "directory": "server"
    }

    # Get all server admins.
    admins = []
    admins = utils.repeat(
        event="select all",
        data=data,
        return_type=list)

    username = session["username"]

    # Color
    for admin in admins:
        if username in admin[0]:
            username += "(<span class=\'admin\'>ADMIN</span>)"
            break

    session["special"] = username
    return session["special"]
