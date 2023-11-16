

class BaseSpider:

    @staticmethod
    def get(url: str) -> "Self":
        """Get a page by url."""
        raise NotImplementedError
