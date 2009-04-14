from abjad.tools import iterate
from abjad.tools import scoretools
from abjad.tuplet.tuplet import _Tuplet


def slip_trivial(expr):
   '''Iterate expr. Slip each trivial tuplet in expr out of score.
      Return None because processes potentially many trivial tuplets.'''
   
   for tuplet in list(iterate.naive(expr, _Tuplet)):
      if tuplet.trivial:
         scoretools.bequeath([tuplet], tuplet[:])
