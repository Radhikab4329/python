import re

text = "The brown fox is running quickly in the meadows"
pattern = r"quickly"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")
