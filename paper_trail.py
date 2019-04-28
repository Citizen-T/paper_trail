import sys
import os

command = sys.argv[1]
if command == 'scan':
    print('Invalid Date(s)')
    print('---------------')
    for path in os.listdir():
        parts = path.split()
        date = parts[0]
        if (len(date) != 10):
            print(path)
