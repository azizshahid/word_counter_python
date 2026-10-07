def count_words(text: str) -> int:
   return len(text.strip(' '))

result = count_words("Hello World")
print(result)