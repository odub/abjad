from abjad.components.Container._MultipliedContainerDurationInterface import _MultipliedContainerDurationInterface
from abjad.tools import mathtools
from fractions import Fraction


class _TupletDurationInterface(_MultipliedContainerDurationInterface):
   r'''Manage duration attributes common to both fixed-duration and fixed-multiplier tuplets.
   '''

   def __init__(self, _client):
      _MultipliedContainerDurationInterface.__init__(self, _client)
      self._preferred_denominator = None

   ## PRVIATE ATTRIBUTES ##

   @property
   def _is_binary(self):
      '''True when multiplier numerator is power of two, otherwise False.
      '''
      if self.multiplier:
         return mathtools.is_power_of_two(self.multiplier.numerator)
      else:
         return True
   
   @property
   def _multiplier_fraction_string(self):
      from abjad.tools import durtools
      if self.preferred_denominator is not None:
         #d, n = durtools.rational_to_duration_pair_with_specified_integer_denominator(
         #   ~self.multiplier, self.preferred_denominator)
         inverse_multiplier = Fraction(self.multiplier.denominator, self.multiplier.numerator)
         d, n = durtools.rational_to_duration_pair_with_specified_integer_denominator(
            inverse_multiplier, self.preferred_denominator)
      else:
         n, d = self.multiplier.numerator, self.multiplier.denominator
      return '%s/%s' % (n, d)

   @property
   def _is_nonbinary(self):
      return not self._is_binary

   ## PUBLIC ATTRIBUTES ##

   @property
   def is_augmentation(self):
      '''True when multiplier is greater than 1.
      Otherwise false::

         abjad> t = tuplettools.FixedDurationTuplet((2, 8), macros.scale(3))
         abjad> t.duration.is_augmentation
         False
      '''

      if self.multiplier:
         return 1 < self.multiplier
      else:
         return False

   @property
   def is_diminution(self):
      '''True when multiplier is less than 1.
      Otherwise false::

         abjad> t = tuplettools.FixedDurationTuplet((2, 8), macros.scale(3))
         abjad> t.duration.is_diminution
         True
      '''

      if self.multiplier:
         return self.multiplier < 1
      else:
         return False

   @apply
   def preferred_denominator( ):
      def fget(self):
         '''.. versionadded:: 1.1.2
         Integer denominator in terms of which tuplet fraction should format.
         '''
         return self._preferred_denominator
      def fset(self, arg):
         if isinstance(arg, (int, long)):
            if not 0 < arg:
               raise ValueError
         elif not isinstance(arg, type(None)):
            raise TypeError
         self._preferred_denominator = arg
      return property(**locals( ))

   @property
   def preprolated(self):
      '''Duration prior to prolation:

      ::

         abjad> t = tuplettools.FixedDurationTuplet((2, 8), macros.scale(3))
         abjad> t.duration.preprolated
         Fraction(1, 4)
      '''

      return self.multiplied
