def count_char(text: str, include_spaces: bool = True) -> int:
    if text.isspace() == True:
        return text.strip()
    return len(text)

result = count_char("Hello world")
print(result)