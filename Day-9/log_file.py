log_file = [
    "ERROR: database connection failed",
    "INFO: operation succesful",
    "ERROR: file not found",
    "DEBUG: connection established",
]

for i in log_file:
    if "DEBUG" in i:
        print(i)
