import re

text = "The brown fox is running quickly in the meadows"
pattern = r"quickly"

match = re.findall(pattern, text)
print(match)
