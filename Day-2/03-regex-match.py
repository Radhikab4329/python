import re

text = "The brown fox is running quickly in the meadows"
pattern = r"quickly"

match = re.match(pattern, text)

if match:
    print("match found:", match.group())
else:
    print("no match")

