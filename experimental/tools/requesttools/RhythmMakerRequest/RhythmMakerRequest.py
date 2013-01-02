from abjad.tools import rhythmmakertools
from experimental.tools.requesttools.Request import Request


class RhythmMakerRequest(Request):
    r'''Rhythm-maker request.

    Create behind-the-scenes at setting-time.
    '''

    ### INTIAILIZER ###

    def __init__(self, payload, request_modifiers=None):
        assert isinstance(payload, rhythmmakertools.RhythmMaker), repr(payload)
        Request.__init__(self, request_modifiers=request_modifiers)
        self._payload = payload

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def payload(self):
        return self._payload
