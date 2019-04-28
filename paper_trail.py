import os

for path in os.listdir():
    parts = path.split()
    date = parts[0]
    if (len(date) != 10):
        print('Date Warning: ' + path)
