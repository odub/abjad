from abjad.tools import abctools
from experimental.symbolictimetools.SymbolicTimespan import SymbolicTimespan


class MixedSourceSymbolicTimespan(SymbolicTimespan):
    r'''.. versionadded:: 1.0

    Mixed-source timespan.

    Mixed-source timespan starting at the left edge of the last measure in the segment 
    with name ``'red'`` and stopping at the right edge of the first measure in the segment 
    with name ``'blue'``::

        >>> segment_selector = selectortools.SingleSegmentSelector(identifier='red')
        >>> inequality = timerelationtools.timespan_2_starts_during_timespan_1(timespan_1=segment_selector.timespan)
        >>> measure_selector = selectortools.BackgroundMeasureSelector(inequality=inequality, start_identifier=-1)
        >>> start_offset = symbolictimetools.SymbolicOffset(selector=measure_selector)

    ::

        >>> segment_selector = selectortools.SingleSegmentSelector(identifier='blue')
        >>> inequality = timerelationtools.timespan_2_starts_during_timespan_1(timespan_1=segment_selector.timespan)
        >>> measure_selector = selectortools.BackgroundMeasureSelector(inequality=inequality, stop_identifier=1)
        >>> stop_offset = symbolictimetools.SymbolicOffset(selector=measure_selector, edge=Right)
        
    ::

        >>> timespan = symbolictimetools.MixedSourceSymbolicTimespan(
        ... start_offset=start_offset, stop_offset=stop_offset)

    ::

        >>> z(timespan)
        symbolictimetools.MixedSourceSymbolicTimespan(
            start_offset=symbolictimetools.SymbolicOffset(
                selector=selectortools.BackgroundMeasureSelector(
                    inequality=timerelationtools.TimespanInequality(
                        'timespan_1.start <= timespan_2.start < timespan_1.stop',
                        timespan_1=symbolictimetools.SingleSourceSymbolicTimespan(
                            selector=selectortools.SingleSegmentSelector(
                                identifier='red'
                                )
                            )
                        ),
                    start_identifier=-1
                    )
                ),
            stop_offset=symbolictimetools.SymbolicOffset(
                selector=selectortools.BackgroundMeasureSelector(
                    inequality=timerelationtools.TimespanInequality(
                        'timespan_1.start <= timespan_2.start < timespan_1.stop',
                        timespan_1=symbolictimetools.SingleSourceSymbolicTimespan(
                            selector=selectortools.SingleSegmentSelector(
                                identifier='blue'
                                )
                            )
                        ),
                    stop_identifier=1
                    ),
                edge=Right
                )
            )

    Mixed-source timespan properties are read-only.
    '''

    ### INITIALIZER ###

    def __init__(self, start_offset=None, stop_offset=None):
        from experimental import symbolictimetools
        assert isinstance(start_offset, (symbolictimetools.SymbolicOffset, type(None))), repr(start_offset)
        assert isinstance(stop_offset, (symbolictimetools.SymbolicOffset, type(None))), repr(stop_offset)
        SymbolicTimespan.__init__(self)
        self._start_offset = start_offset
        self._stop_offset = stop_offset

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        '''True when `expr` equals self. Otherwise false.

        Return boolean.
        '''
        if isintance(expr, type(self)):
            if self.start_offset == timespan_2.start_offset:
                if self.stop_offset == timespan_2.stop_offset:
                    return True
        return False

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def start_offset(self):
        '''Mixed-source timespan start offset specified by user.

        Return offset or none.
        '''
        return self._start_offset

    @property
    def stop_offset(self):
        '''Mixed-source timepsan stop offset specified by user.

        Return offset or none.
        '''
        return self._stop_offset

    ### PUBLIC METHODS ###

    def get_score_start_offset(self, score_specification, context_name):
        '''Evaluate score start offset of symbolic timespan when applied
        to `context_name` in `score_specification`.

        .. note:: not yet implemented.

        Return offset.
        '''
        raise NotImplementedError

    def get_score_stop_offset(self, score_specification, context_name):
        '''Evaluate score stop offset of symbolic timespan when applied
        to `context_name` in `score_specification`.

        .. note:: not yet implemented.

        Return offset.
        '''
        raise NotImplementedError

    def set_segment_identifier(self, segment_identifier):
        '''.. note:: not yet implemented.
        '''
        raise NotImplementedError
