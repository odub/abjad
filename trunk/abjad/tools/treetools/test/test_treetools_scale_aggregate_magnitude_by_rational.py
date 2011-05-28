from abjad.tools.treetools import *
from abjad.tools.treetools._make_test_blocks import _make_test_blocks
from fractions import Fraction
import py.test


def test_treetools_scale_aggregate_magnitude_by_rational_01( ):
   a = BoundedInterval(Fraction(-1, 2), 1)
   b = BoundedInterval(2, Fraction(7, 3))
   tree = IntervalTree([a, b])
   rational = 2
   result = scale_aggregate_magnitude_by_rational(tree, rational)
   assert result.magnitude == tree.magnitude * rational
   assert [x.signature for x in result] == \
      [(Fraction(-1, 2), Fraction(5, 2)), (Fraction(9, 2), Fraction(31, 6))]

def test_treetools_scale_aggregate_magnitude_by_rational_02( ):
   a = BoundedInterval(Fraction(-1, 2), 1)
   b = BoundedInterval(2, Fraction(7, 3))
   tree = IntervalTree([a, b])
   rational = -1
   py.test.raises(AssertionError,
      "result = scale_aggregate_magnitude_by_rational(tree, rational)")

def test_treetools_scale_aggregate_magnitude_by_rational_03( ):
   a = BoundedInterval(Fraction(-1, 2), 1)
   b = BoundedInterval(2, Fraction(7, 3))
   tree = IntervalTree([a, b])
   rational = 0
   py.test.raises(AssertionError, 
      "result = scale_aggregate_magnitude_by_rational(tree, rational)")
