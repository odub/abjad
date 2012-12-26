from abjad import *


def test_RhythmTreeContainer_contents_duration_01(): 

    leaf_a = rhythmtreetools.RhythmTreeLeaf(duration=3)
    leaf_b = rhythmtreetools.RhythmTreeLeaf(duration=3)
    leaf_c = rhythmtreetools.RhythmTreeLeaf(duration=2)
    subcontainer = rhythmtreetools.RhythmTreeContainer(duration=2, children=[leaf_b, leaf_c])
    leaf_d = rhythmtreetools.RhythmTreeLeaf(duration=1)

    container = rhythmtreetools.RhythmTreeContainer(duration=1, children=[leaf_a, subcontainer, leaf_d])
    
    assert container.contents_duration == 6
    assert subcontainer.contents_duration == 5
