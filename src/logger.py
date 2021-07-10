import sys


class Logger:
    def __init__(self, filename):
        try:
            self.file = open(filename, "w+")
        except IOError:
            print("error opening history file")
            sys.exit(1)

    def log(self, message):
        self.file.write(message)

    def log_error(self, message):
        self.file.write(message)
