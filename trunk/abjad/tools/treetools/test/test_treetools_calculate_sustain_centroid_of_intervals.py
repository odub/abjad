from abjad.tools.treetools import *
from abjad.tools.treetools._make_test_blocks import _make_test_blocks
from fractions import Fraction


def test_treetools_calculate_sustain_centroid_of_intervals_01( ):
   tree = IntervalTree(_make_test_blocks( ))
   result = calculate_sustain_centroid_of_intervals(tree)
   assert result == Fraction(1619, 90)


def test_treetools_calculate_sustain_centroid_of_intervals_02( ):
   tree = IntervalTree([ ])
   result = calculate_sustain_centroid_of_intervals(tree)
   assert result is None
