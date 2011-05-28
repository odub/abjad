from abjad.tools.treetools.BoundedInterval import BoundedInterval
from abjad.tools.treetools.IntervalTree import IntervalTree
from abjad.tools.treetools.all_are_intervals_or_trees_or_empty import all_are_intervals_or_trees_or_empty
from abjad.tools.treetools.get_all_unique_bounds_in_intervals import get_all_unique_bounds_in_intervals
from abjad.tools.treetools.split_intervals_at_rationals import split_intervals_at_rationals


def compute_depth_of_intervals(intervals):
   '''Compute a tree whose intervals represent the depth (level of overlap) 
   in each boundary pair of `intervals`::

      abjad> from abjad.tools.treetools import *
      abjad> a = BoundedInterval(0, 3)
      abjad> b = BoundedInterval(6, 12)
      abjad> c = BoundedInterval(9, 15)
      abjad> tree = IntervalTree([a, b, c])
      abjad> compute_depth_of_intervals(tree)
      IntervalTree([
         BoundedInterval(0, 3, data = {'depth': 1}),
         BoundedInterval(3, 6, data = {'depth': 0}),
         BoundedInterval(6, 9, data = {'depth': 1}),
         BoundedInterval(9, 12, data = {'depth': 2}),
         BoundedInterval(12, 15, data = {'depth': 1})
      ])
   '''

   assert all_are_intervals_or_trees_or_empty(intervals)
   if isinstance(intervals, IntervalTree):
      tree = intervals
   else:
      tree = IntervalTree(intervals)

   bounds = list(get_all_unique_bounds_in_intervals(tree))
   intervals = [ ]
   for i in range(len(bounds) - 1):
      target = BoundedInterval(bounds[i], bounds[i+1], { })
      found = tree.find_intervals_intersecting_or_tangent_to_interval(target)
      if found:
         depth = len(filter(lambda x: not x.low == target.high and not x.high == target.low, found))
      else:
         depth = 0
      target.data['depth'] = depth
      intervals.append(target)

   return IntervalTree(intervals)
