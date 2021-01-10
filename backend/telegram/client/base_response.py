class BaseResponse(object):
    def __init__(self):
        self.success = None
        self.message = None
        self.error_code = None
        self.data = None

    def done(self, message=None, data=None) -> 'BaseResponse':
        self.success = True
        self.message = message
        self.data = data
        return self

    def fail(self, message: str = "No Telegram client is ready...", error_code: int = None) -> 'BaseResponse':
        self.success = False
        self.message = message
        self.error_code = error_code
        return self
