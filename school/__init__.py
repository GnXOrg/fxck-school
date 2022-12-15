from importlib import import_module
from pathlib import Path

def exec_file(file: str | Path):
    if isinstance(file, Path):
        file = str(file)
    import_module("." + file, package=__name__)
