class Result:

    def __init__(self, message, result):
        self.message = message
        self.result = result

    @property
    def loginResult(self):
        return self

    @loginResult.setter
    def set(self, errorCode, message, result):
        self.errorCode = errorCode
        self.message = message
        self.result = result

    def get(self):
        return self
