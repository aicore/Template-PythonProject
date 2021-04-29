import sys
import pathlib
import module_example
# Entry point main of the program. This will also add the current folder
# /src/main/python to path so that all modules within the dir are picked up correctly.
# Keep this path insert call at the entry point of your py src.
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, str(pathlib.Path(__file__).parent.absolute()))


def main_handler(args):
    return module_example.hello_module(args)
