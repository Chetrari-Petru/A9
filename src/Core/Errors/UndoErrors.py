class UndoError(Exception):
    pass

class UndoNotPossibleError(UndoError):
    pass

class RedoNotPossibleError(UndoError):
    pass