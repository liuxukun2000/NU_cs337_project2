import re


def get_servings(inp: str) -> int:
    regex = r"\d+"
    ans = re.findall(regex, inp)
    return sum([int(x) for x in ans]) // len(ans) if len(ans) else 0