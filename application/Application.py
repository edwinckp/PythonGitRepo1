from builtins import object


class Application(object):
    """ Application """

    _allowed_states = ['New', 'Initialized', 'Moved']
    _state = None

    def __init__(self):
        self._state = 'Initialized'

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state=None):
        if state in self._allowed_states:
            self._state = state
