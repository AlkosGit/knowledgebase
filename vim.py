# File: vim.py
from listprops import ListProps

class Doc(ListProps):
    """
    Install python extension to vim:
        # dnf install python3-jedi vim-jedi

    Vim keys:
        :sp <filename> - split screen with second file (vertically)
        :vs <filename> - split screen with second file (horizontally)
        / <string> - search for <string> in current file
        n - find next <string>
    """
