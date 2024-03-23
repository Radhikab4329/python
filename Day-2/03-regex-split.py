import re

text = "grape,banana,apple,orange"
pattern = r","

split_result = re.split(pattern, text)
print(split_result)

