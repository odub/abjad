# -*- encoding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import durationtools
from abjad.tools.abctools import AbjadObject


class QTargetBeat(AbjadObject):
    r'''Representation of a single "beat" in a quantization target:

    ::

        >>> beatspan = (1, 8)
        >>> offset_in_ms = 1500
        >>> search_tree = quantizationtools.UnweightedSearchTree({3: None})
        >>> tempo = indicatortools.Tempo((1, 4), 56)

    ::

        >>> q_target_beat = quantizationtools.QTargetBeat(
        ...     beatspan=beatspan,
        ...     offset_in_ms=offset_in_ms,
        ...     search_tree=search_tree,
        ...     tempo=tempo,
        ...     )

    ::

        >>> q_target_beat
        quantizationtools.QTargetBeat(
            beatspan=durationtools.Duration(1, 8),
            offset_in_ms=durationtools.Offset(1500, 1),
            search_tree=quantizationtools.UnweightedSearchTree(
                definition={   3: None,
                    },
                ),
            tempo=indicatortools.Tempo(
                durationtools.Duration(1, 4),
                56
                ),
            )

    Not composer-safe.

    Used internally by quantizationtools.Quantizer.

    Return ``QTargetBeat`` instance.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_beatspan',
        '_distances',
        '_grouping',
        '_offset_in_ms',
        '_q_events',
        '_q_grid',
        '_q_grids',
        '_search_tree',
        '_tempo',
        )

    ### INITIALIZER ###

    def __init__(self,
        beatspan=None,
        offset_in_ms=None,
        search_tree=None,
        tempo=None,
        ):
        from abjad.tools import quantizationtools

        beatspan = durationtools.Duration(beatspan)
        offset_in_ms = durationtools.Offset(offset_in_ms)

        if search_tree is None:
            search_tree = quantizationtools.UnweightedSearchTree()
        assert isinstance(search_tree, quantizationtools.SearchTree)
        tempo = indicatortools.Tempo(tempo)
        assert not tempo.is_imprecise

        q_events = []
        q_grids = []

        self._beatspan = beatspan
        self._distances = {}
        self._offset_in_ms = offset_in_ms
        self._q_events = q_events
        self._q_grid = None
        self._q_grids = q_grids
        self._search_tree = search_tree
        self._tempo = tempo

    ### SPECIAL METHODS ###

    def __call__(self, job_id):
        from abjad.tools import quantizationtools
        if not self.q_events:
            return None
        assert all(isinstance(x, quantizationtools.QEvent)
            for x in self.q_events)
        q_event_proxies = []
        for q_event in self.q_events:
            q_event_proxy = quantizationtools.QEventProxy(
                q_event,
                self.offset_in_ms,
                self.offset_in_ms + self.duration_in_ms,
                )
            q_event_proxies.append(q_event_proxy)
        return quantizationtools.QuantizationJob(
            job_id, self.search_tree, q_event_proxies)

    def __format__(self, format_specification=''):
        r'''Formats q-event.

        Set `format_specification` to `''` or `'storage'`.
        Interprets `''` equal to `'storage'`.

        Returns string.
        '''
        from abjad.tools import systemtools
        if format_specification in ('', 'storage'):
            return systemtools.StorageFormatManager.get_storage_format(self)
        return str(self)

    def __repr__(self):
        return format(self)

    ### PUBLIC PROPERTIES ###

    @property
    def beatspan(self):
        r'''The beatspan of the ``QTargetBeat``:

        ::

            >>> q_target_beat.beatspan
            Duration(1, 8)

        Returns Duration.
        '''
        return self._beatspan

    @property
    def distances(self):
        r'''A list of computed distances between the ``QEventProxies``
        associated with a ``QTargetBeat`` instance, and each ``QGrid``
        generated for that beat.

        Used internally by the ``Quantizer``.

        Returns tuple.
        '''
        return self._distances

    @property
    def duration_in_ms(self):
        r'''The duration in milliseconds of the ``QTargetBeat``:

        ::

            >>> q_target_beat.duration_in_ms
            Duration(3750, 7)

        Returns Duration instance.
        '''
        from abjad.tools import quantizationtools
        return self.tempo.duration_to_milliseconds(self.beatspan)

    @property
    def offset_in_ms(self):
        r'''The offset in milliseconds of the ``QTargetBeat``:

        ::

            >>> q_target_beat.offset_in_ms
            Offset(1500, 1)

        Returns Offset instance.
        '''
        return self._offset_in_ms

    @property
    def q_events(self):
        r'''A list for storing ``QEventProxy`` instances.

        Used internally by the ``Quantizer``.

        Returns list.
        '''
        return self._q_events

    @property
    def q_grid(self):
        r'''The ``QGrid`` instance selected by a ``Heuristic``.

        Used internally by the ``Quantizer``.

        Return ``QGrid`` instance.
        '''
        return self._q_grid

    @property
    def q_grids(self):
        r'''A tuple of ``QGrids`` generated by a ``QuantizationJob``.

        Used internally by the ``Quantizer``.

        Returns tuple.
        '''
        return self._q_grids

    @property
    def search_tree(self):
        r'''The search tree of the ``QTargetBeat``:

        ::

            >>> q_target_beat.search_tree
            UnweightedSearchTree(
                definition={   3: None}
                )

        Return ``SearchTree`` instance.
        '''
        return self._search_tree

    @property
    def tempo(self):
        r'''The tempo of the ``QTargetBeat``:

        ::

            >>> q_target_beat.tempo
            Tempo(Duration(1, 4), 56)

        Return ``Tempo`` instance.
        '''
        return self._tempo
