import sys
import json


class Logger:
    def __init__(self, filename):
        try:
            self.filename = filename
            self.file = open(filename, "r+")
            self.history = json.load(self.file)
        except IOError:
            print("error opening history file")
            sys.exit(1)

    def log(self, message):
        self.history["journal"].append(message)

    def log_error(self, message):
        self.history["error"].append(message)

    def save(self):
        self.file.seek(0)
        json.dump(self.history, self.file)


logger = Logger("history.json")


def log(func):
    def wrap_func(*args, **kwargs):
        logger.log(f"{func.__doc__} {args}")
        res = func(*args, **kwargs)
        logger.save()
        return res

    return wrap_func
