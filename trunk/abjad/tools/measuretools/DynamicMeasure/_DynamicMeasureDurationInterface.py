from abjad.components.Measure._MeasureDurationInterface import _MeasureDurationInterface


class _DynamicMeasureDurationInterface(_MeasureDurationInterface):

   ## PUBLIC ATTRIBUTES ##

   @property
   def preprolated(self):
      return self.contents
