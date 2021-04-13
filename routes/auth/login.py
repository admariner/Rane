from flask import request, session, redirect, url_for
from utils import utils, user_utils, chat_utils
import hashlib
import create_app


def login():
    app = create_app.app
    app.logger.info("Going to room 0")

    username = request.form["login-username"]
    password = hashlib.sha256(request.form["login-password"].encode()).hexdigest()

    data = {
        "filename": "accounts",
        "folder": "server",
        "table": "accounts",
        "select": "username, password",
        "where": f"username=\"{username}\" and password=\"{password}\""
    }

    # Check
    ret = utils.repeat(
        event="retrieve table",
        data=data,
        return_type=list
    )

    if ret:
        session["username"] = username

        user_utils.online(1, 0)
        chat_utils.autocolor()

        return redirect(url_for("room", room_id=0))

    session["login_error"] = "Invalid Username or Password"
    return redirect("/")