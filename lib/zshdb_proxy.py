#!/usr/bin/env python3

"""
Run zshdb in a pty.

This will allow to inject server commands not exposing them
to a user.
"""

import re
from bashdb_proxy import BashDBProxy


class ZshDBProxy(BashDBProxy):
    """PTY proxy for zshdb."""

    # zshdb adds a lot of control sequences, careful.
    PROMPT = re.compile(r'{0}zshdb<\(?\d+\)?>{0} {0}'
                        .format(r"(\[[^a-zA-Z]*[a-zA-Z])*")
                        .encode('ascii'))

    def __init__(self):
        """ctor."""
        super().__init__("ZshDB")


if __name__ == '__main__':
    ZshDBProxy().run()
