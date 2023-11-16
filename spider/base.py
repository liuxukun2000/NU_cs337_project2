

class BaseSpider:

    @staticmethod
    def name() -> str:
        """The url of the website."""
        raise NotImplementedError

    @staticmethod
    def get(url: str) -> "Self":
        """Get a page by url."""
        raise NotImplementedError
