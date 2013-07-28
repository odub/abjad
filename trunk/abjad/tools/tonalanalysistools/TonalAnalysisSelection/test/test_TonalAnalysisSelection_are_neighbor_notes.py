from abjad import *


def test_TonalAnalysisSelection_are_neighbor_notes_01():

    notes = notetools.make_notes([0, 2, 4, 2, 0], [(1, 4)])
    staff = Staff(notes)

    selection = tonalanalysistools.select(staff[:])
    result = selection.are_neighbor_notes()
    result == [False, False, True, False, False]
