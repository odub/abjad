from abjad.tools.pitchtools._Vector import _Vector


class InversionEquivalentChromaticIntervalClassVector(_Vector):
   '''.. versionadded:: 1.1.2

   Abjad model of inversion-equivalent chromatic interval-class vector::

      abjad> pitchtools.InversionEquivalentChromaticIntervalClassVector([1, 1, 6, 2, 2, 2])
      InversionEquivalentChromaticIntervalClassVector(0 | 2 3 0 0 0 1)

   Inversion-equivalent chromatic interval-class vectors are immutable.
   '''

   def __init__(self, interval_class_tokens):
      from abjad.tools import pitchtools
      for icn in range(7):
         dict.__setitem__(self, icn, 0)
         dict.__setitem__(self, icn + 0.5, 0)
      dict.__delitem__(self, 6.5)
      for token in interval_class_tokens:
         interval_class_number = pitchtools.InversionEquivalentChromaticIntervalClass(token).number
         current_tally = self[interval_class_number]
         dict.__setitem__(self, interval_class_number, current_tally + 1)

   ## OVERLOADS ##

   def __repr__(self):
      return '%s(%s)' % (self.__class__.__name__, self._format_string)

   ## PRIVATE ATTRIBUTES ##

   @property
   def _format_string(self):
      string = '%s | %s' % (
         self._unison_string, self._nonunison_twelve_tone_string)
      if self._has_quartertones:
         string += ' %s' % self._quartertone_string
      return string
      
   @property
   def _has_quartertones(self):
      return any([0 < item[1] for item in self._quartertone_items])

   @property
   def _nonunison_twelve_tone_string(self):
      return ' '.join(self._twelve_tone_string.split( )[1:])

   @property
   def _quartertone_items(self):
      return [item for item in self.items( ) if isinstance(item[0], float)]

   @property
   def _quartertone_string(self):
      return ' '.join([
         str(item[1]) for item in sorted(self._quartertone_items)])
         
   @property
   def _twelve_tone_items(self):
      return [item for item in self.items( ) if isinstance(item[0], int)]

   @property
   def _twelve_tone_string(self):
      return ' '.join([
         str(item[1]) for item in sorted(self._twelve_tone_items)])

   @property
   def _unison_string(self):
      return self._twelve_tone_string.split( )[0]
