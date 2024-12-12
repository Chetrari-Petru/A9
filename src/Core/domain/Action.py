class Action:
    _action = None
    _action_parameters = None
    _reverse_action = None
    _reverse_action_parameters = None

    def __init__(self, action, reverse_action, action_parameters, reverse_action_parameters):
        self._action = action
        self._reverse_action = reverse_action
        self._action_parameters = action_parameters
        self._reverse_action_parameters = reverse_action_parameters

    def undo(self):
        self._reverse_action(**self._reverse_action_parameters)

    def redo(self):
        self._action(**self._action_parameters)


