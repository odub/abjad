from abjad.exceptions import MissingSpannerError
from abjad.tools import componenttools
from abjad.tools import spannertools


def are_components_in_same_tie_spanner(components):
   '''True if all components in list share same tie spanner,
      otherwise False.

   .. versionchanged:: 1.1.2
      renamed ``tietools.are_in_same_spanner( )`` to
      ``tietools.are_components_in_same_tie_spanner( )``.
   '''

   assert componenttools.all_are_components(components)
   
   try:
      first = components[0]
      try:
         #first_tie_spanner = first.tie.spanner
         first_tie_spanner = spannertools.get_the_only_spanner_attached_to_component(
            first, spannertools.TieSpanner)
         for component in components[1:]:
            #if component.tie.spanner is not first_tie_spanner:
            component_tie_spanner = spannertools.get_the_only_spanner_attached_to_component(
               component, spannertools.TieSpanner)
            if component_tie_spanner is not first_tie_spanner:
               return False
      except MissingSpannerError:
         return False
   except IndexError:
      return True

   return True
