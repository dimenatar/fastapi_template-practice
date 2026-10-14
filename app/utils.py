import re


def camel_to_snake(line: str) -> str:
    s1 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", line)
    return s1.lower()
