import os

from chainlit.utils import mount_chainlit
from fastapi import FastAPI


def get_app_path() -> str:
    import importlib  # noqa: PLC0415

    target = os.getenv("TARGET", "ch5_4")
    targets = {
        "ch5_0",
        "ch5_4",
        "ch5_5",
        "ch5_6",
        "ch5_7",
        "ch5_8",
    }
    if target not in targets:
        msg = f"Unknown target: {target}"
        raise ValueError(msg)
    module = importlib.import_module(f"chainlit_playground.{target}.app")
    assert module.__file__ is not None
    return module.__file__


def app() -> FastAPI:
    app = FastAPI()
    target = get_app_path()
    mount_chainlit(app, target, path="/")
    return app
