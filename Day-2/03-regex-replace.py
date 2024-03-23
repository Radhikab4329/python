import re

text = "The quick brown fox jumps over the brown lazy dog"
pattern = r"brown"

replacement = "yellow"
new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
