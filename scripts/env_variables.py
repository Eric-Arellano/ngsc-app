from scripts.utils import sys_calls


def set_backend() -> None:
    sys_calls.export("FLASK_APP", "backend/src/server.py")
