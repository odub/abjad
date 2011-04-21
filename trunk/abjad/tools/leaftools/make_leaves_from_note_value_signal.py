from abjad.components import Note
from abjad.components import Rest
from abjad.tools.leaftools.make_leaves import make_leaves


def make_leaves_from_note_value_signal(note_value_signal, unit_of_signal, tied_rests = False):
   r'''.. versionadded:: 1.1.2

   Make leaves from `note_value_signal` and `unit_of_signal`::

      abjad> leaves = leaftools.make_leaves_from_note_value_signal([3, -3, 5, -5], Fraction(1, 8))
      abjad> staff = Staff(leaves)

   ::

      abjad> f(staff)
      \new Staff {
         c'4.
         r4.
         c'2 ~
         c'8
         r2
         r8
      }

   Interpret positive elements in `note_value_signal` as notes.

   Interpret negative elements in `note_value_signal` as rests.

   Set the pitch of all notes to middle C.

   Return list of notes and / or rests.
   '''

   result = [ ]

   for note_value in note_value_signal:
      if note_value == 0:
         raise ValueError('note values must be nonzero.')
      elif 0 < note_value:
         leaves = make_leaves([0], [note_value * unit_of_signal])
      else:
         leaves = make_leaves([None], [-note_value * unit_of_signal], tied_rests = tied_rests)
      result.extend(leaves)

   return result
