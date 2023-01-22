"""
This cli.py script is the entry point for the Biking-Berlin game. (This
entry-point script is all that is necessary to use this project with
PyInstaller.)
It calls main() to start it up.
"""

from biking_berlin.__main__ import main_game_loop # type: ignore

if __name__ == '__main__':
    main_game_loop()
