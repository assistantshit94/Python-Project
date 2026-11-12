import os

print("Current directory:", os.getcwd())
print("File exists:", os.path.exists("log.txt"))

with open("log.txt", "r") as f:
    content = f.read()

print("Actual content:", repr(content))
print("Python found:", "python" in content.lower())