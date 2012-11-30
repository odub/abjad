import abc
from abjad.tools.abctools.AbjadObject import AbjadObject
from experimental import helpertools


class Request(AbjadObject):
    r'''.. versionadded:: 1.0

    Base class from which other request classes inherit.

    Requests function as setting sources.
    '''

    ### CLASS ATTRIBUTES ###

    __metaclass__ = abc.ABCMeta

    attributes = helpertools.AttributeNameEnumeration()

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(self, index=None, count=None, reverse=None, rotation=None, callback=None):
        assert isinstance(index, (int, type(None))), repr(index)
        assert isinstance(count, (int, type(None))), repr(count)
        assert isinstance(reverse, (bool, type(None))), repr(reverse)
        assert isinstance(rotation, (int, type(None))), repr(rotation)
        assert isinstance(callback, (helpertools.Callback, type(None))), repr(callback)
        self._index = index
        self._count = count
        self._reverse = reverse
        self._rotation = rotation
        self._callback = callback

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        '''True when mandatory and keyword arguments compare equal.
        Otherwise false.

        Return boolean.
        '''
        if not isinstance(expr, type(self)):
            return False
        if not self._mandatory_argument_values == expr._mandatory_argument_values:
            return False
        return self._keyword_argument_values == expr._keyword_argument_values

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def callback(self):
        return self._callback

    @property
    def count(self):
        return self._count

    @property
    def index(self):
        return self._index

    @property
    def reverse(self):
        return self._reverse

    @property
    def rotation(self):
        return self._rotation
