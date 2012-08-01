from itertools import groupby
from abjad.tools import notetools
from abjad.tools import resttools
from abjad.tools.componenttools import all_are_contiguous_components_in_same_thread
from abjad.tools.contexttools import TempoMark
from abjad.tools.contexttools import get_effective_tempo
from abjad.tools.durationtools import Offset
from experimental.quantizationtools.QEvent import QEvent
from experimental.quantizationtools.millisecond_pitch_pairs_to_q_events \
    import millisecond_pitch_pairs_to_q_events
from experimental.quantizationtools.tempo_scaled_rational_to_milliseconds \
    import tempo_scaled_rational_to_milliseconds
from abjad.tools import skiptools
from abjad.tools.tietools import get_tie_chain


def tempo_scaled_leaves_to_q_events(leaves, tempo=None):
    '''Convert `leaves` to a list of :py:class:`~abjad.tools.quantizationtools.QEvent` objects.
    If the leaves have no effective tempo, `tempo` must be a
    :py:class:`~abjad.tools.contexttools.TempoMark`.

    ::

        >>> from experimental.quantizationtools import tempo_scaled_leaves_to_q_events
        >>> source = Staff("c'4 r4. e'8 <g' b' d'' fs''>2")
        >>> source_tempo = contexttools.TempoMark((1, 4), 55)
        >>> for x in tempo_scaled_leaves_to_q_events(source[:], tempo=source_tempo): x
        ...
        quantizationtools.PitchedQEvent(
            durationtools.Offset(0, 1),
            (NamedChromaticPitch("c'"),),
            attachments=()
            )
        quantizationtools.SilentQEvent(
            durationtools.Offset(12000, 11),
            attachments=()
            )
        quantizationtools.PitchedQEvent(
            durationtools.Offset(30000, 11),
            (NamedChromaticPitch("e'"),),
            attachments=()
            )
        quantizationtools.PitchedQEvent(
            durationtools.Offset(36000, 11),
            (NamedChromaticPitch("g'"), NamedChromaticPitch("b'"), NamedChromaticPitch("d''"), NamedChromaticPitch("fs''")),
            attachments=()
            )
        quantizationtools.TerminalQEvent(
            durationtools.Offset(60000, 11)
            )

    Return a list of :py:class:`~abjad.tools.quantizationtools.QEvent` objects.
    '''

    assert all_are_contiguous_components_in_same_thread(leaves) and len(leaves)
    if tempo is None:
        assert get_effective_tempo(leaves[0]) is not None
    else:
        assert isinstance(tempo, TempoMark)

    # sort by silence and tied leaves
    groups = []
    for rvalue, rgroup in groupby(leaves, lambda x: isinstance(x, (resttools.Rest, skiptools.Skip))):
        if rvalue:
            groups.append(list(rgroup))
        else:
            for tvalue, tgroup in groupby(rgroup, lambda x: get_tie_chain(x)):
                groups.append(list(tgroup))

    # calculate lists of pitches and durations
    durations = []
    pitches = []
    for group in groups:

        # get millisecond cumulative duration
        if tempo is not None:
            duration = sum([tempo_scaled_rational_to_milliseconds(x.prolated_duration, tempo)
                for x in group])
        else:
            duration = sum([tempo_scaled_rational_to_milliseconds(x.prolated_duration,
                get_effective_tempo(x)) for x in group])
        durations.append(duration)

        # get pitch of first leaf in group
        if isinstance(group[0], (resttools.Rest, skiptools.Skip)):
            pitch = None
        elif isinstance(group[0], notetools.Note):
            pitch = group[0].written_pitch.chromatic_pitch_number
        else: # chord
            pitch = [x.written_pitch.chromatic_pitch_number for x in group[0].note_heads]
        pitches.append(pitch)

    # convert durations and pitches to QEvents and return
    return millisecond_pitch_pairs_to_q_events(zip(durations, pitches))
