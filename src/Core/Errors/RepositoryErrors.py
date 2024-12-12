class RepositoryError(Exception):
    def __init__(self, message):
        super().__init__(message)

class ObjectNotFoundError(RepositoryError):
    def __init__(self, message):
        super().__init__(message)

class FileIsEmptyError(RepositoryError):
    def __init__(self):
        super().__init__("File is empty")

class NothingImportedError(RepositoryError):
    def __init__(self):
        super().__init__("Nothing imported")
