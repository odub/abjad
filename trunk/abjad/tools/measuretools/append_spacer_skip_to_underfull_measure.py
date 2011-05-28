from abjad.components import Measure
from abjad.tools import contexttools
from abjad.tools.skiptools.Skip import Skip


def append_spacer_skip_to_underfull_measure(rigid_measure):
   r'''.. versionadded:: 1.1.1

   Append spacer skip to underfull `measure`::

      abjad> measure = Measure((4, 12), macros.scale(4))
      abjad> contexttools.TimeSignatureMark(5, 12)(measure)
      abjad> measure.duration.is_underfull 
      True
      
   ::
      
      abjad> measuretools.append_spacer_skip_to_underfull_measure(measure) 
      Measure(5/12, [c'8, d'8, e'8, f'8, s1 * 1/8])
      
   ::
      
      abjad> f(measure)
      {
         \time 5/12
         \scaleDurations #'(2 . 3) {
            c'8
            d'8
            e'8
            f'8
            s1 * 1/8
         }
      }

   Append nothing to nonunderfull `measure`.

   Return `measure`.

   .. versionchanged:: 1.1.2
      renamed ``measuretools.make_measures_with_full_measure_spacer_skips_underfull_spacer_skip( )`` to
      ``measuretools.append_spacer_skip_to_underfull_measure( )``.
   '''

   assert isinstance(rigid_measure, Measure)

   if rigid_measure.duration.is_underfull:
      target_duration = contexttools.get_effective_time_signature(rigid_measure).duration
      prolated_duration = rigid_measure.duration.prolated
      skip = Skip((1, 1))
      meter_multiplier = contexttools.get_effective_time_signature(rigid_measure).multiplier
      new_multiplier = (target_duration - prolated_duration) / meter_multiplier
      skip.duration.multiplier = new_multiplier
      rigid_measure.append(skip)

   return rigid_measure
