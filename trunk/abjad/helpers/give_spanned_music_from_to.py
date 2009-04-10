from abjad.exceptions.exceptions import MusicContentsError
from abjad.helpers.assert_components import assert_components
from abjad.tools import parenttools


def _give_spanned_music_from_to(donors, recipient):
   '''Give any music belong to donor components 'donors'
      to recipient component 'recipient'.
      Works great when 'recipient' is an empty container.
      Pass silently when recipient is a nonempty container 
      or a leaf and when donors have no music.
      Raises MusicContentsError when donors *do* have music
      to music but when recipient is unable to accept music
      (because recipient is nonempty container or leaf).

      Return donor components 'donors'.

      Helper is not composer-safe and may cause discontiguous spanners.'''

   from abjad.container.container import Container
   from abjad.leaf.leaf import _Leaf
   assert_components(donors, contiguity = 'strict', share = 'parent')

   ## if recipient is leaf or nonempty container, 
   ## make sure there's no music in donor components to hand over
   if isinstance(recipient, _Leaf) or \
      (isinstance(recipient, Container) and len(recipient)):
      if all([len(x.music) == 0 for x in donors]):
         return donors
      else:
         raise MusicContentsError('can not give music to leaf.')
      
   ## otherwise recipient is empty container, so proceed
   ## collect music from all donor components
   donor_music = [ ]
   for donor in donors:
      donor_music.extend(donor.music)

   ## give music from donor components to recipient component
   recipient._music.extend(donor_music)
   parenttools.switch(recipient[:], recipient)

   ## return donor components
   return donors
