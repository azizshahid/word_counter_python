def count_words(text: str) -> int:
   return len(text.split())

result = count_words("well-known fact")
print(result)