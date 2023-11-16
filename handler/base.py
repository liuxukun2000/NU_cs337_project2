from typing import Dict, Any


class BaseHandler:

    @staticmethod
    def type() -> str:
        """The type of the handler."""
        raise NotImplementedError
    def match(self, inp: str, cfg: Dict[str, Any]) -> int:
        """Return whether the handler matches the input."""
        raise NotImplementedError

    def handle(self, inp: str, cfg: Dict[str, Any]) -> str:
        """Handle the input."""
        raise NotImplementedError