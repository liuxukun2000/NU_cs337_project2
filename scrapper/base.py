

class BaseSpider:

    @staticmethod
    def name() -> str:
        """The url of the website."""
        raise NotImplementedError

    @staticmethod
    def get(url: str) -> "Self":
        """Get a page by url."""
        raise NotImplementedError

    def transform(self, ori, target):
        # return
        for i in self.steps:
            i.text = i.text.replace(ori, target)

    def __str__(self):
        return f"**{self.title}**\n\n**Ingredients:**\n\n" + "\n\n".join(map(str, self.ingredients)) + "\n\n**Steps:**\n\n" + "\n\n".join([i.to_string() for i in self.steps]) +\
    f"\n\nServings\n\n{self.servings}"