import json
characters = list(input('Enter string: '))

counted_chars = {}
char_count = 0

for char in characters:
    if char != ' ':
        counted_chars[char] = characters.count(char)
        char_count += 1

for key in counted_chars:
    percentual_appearance = (counted_chars[key] / char_count) * 100
    counted_chars[key] = round(percentual_appearance, 2)

print(json.dumps(counted_chars, indent=4))
