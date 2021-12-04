class myException(Exception):
    def __init__(self, msg):
        self.msg = msg


error = myException("Something went wrong")

