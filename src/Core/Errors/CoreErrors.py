class CoreError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidRepositoryError(CoreError):
    def __init__(self, message):
        super().__init__(message)

class CannotRentError(CoreError):
    def __init__(self, message):
        super().__init__(message)