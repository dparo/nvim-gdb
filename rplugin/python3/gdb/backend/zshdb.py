"""ZshDB specifics."""

from gdb.backend import bashdb


class ZshDB(bashdb.BashDB):
    """ZshDB FSM."""

    def create_parser_impl(self, common, handler):
        """Create parser implementation instance."""
        return bashdb.ParserImpl(common, handler, "zshdb")
