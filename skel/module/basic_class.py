class ##PROJECT##(object):
    __slots__ = ["_msg"]

    def __init__(self):
        self._msg = "Hello from module ##PROJECT##"

    def ##PROJECT##(self, name: str):
        print("%s, %s!" % (self._msg, name))
