import sys
import os

class Scanner:
    def __init__(self, path):
        self.path = path
    def countFiles(self):
        count = len(os.listdir(self.path))
        return count

def other():
    command = sys.argv[1]
    if command == 'scan':
        print('Invalid Date(s)')
        print('---------------')
        for path in os.listdir():
            parts = path.split()
            date = parts[0]
            if (len(date) != 10):
                print(path)
