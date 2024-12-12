class IdGeneratorError(Exception):
    def __init__(self, message):
        super().__init__(message)


class IdNotFoundError(IdGeneratorError):
    pass
    # def __init__(self, message):
    #     super().__init__(message)


class IdRemovedError(IdGeneratorError):
    pass
    # def __init__(self, message):
    #     super().__init__(message)