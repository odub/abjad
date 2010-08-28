from abjad.core import Rational
from abjad.tools.spannertools.Spanner._SpannerFormatInterface import _SpannerFormatInterface
from abjad.tools import marktools


class _MetricGridSpannerFormatInterface(_SpannerFormatInterface):

   def __init__(self, spanner):
      _SpannerFormatInterface.__init__(self, spanner)

   ## PUBLIC METHODS ##

   def _after(self, leaf):
      '''Spanner format contribution after leaf.'''
      result = [ ]
      spanner = self.spanner
      if hasattr(spanner, '_slicing_metersFound'):
         delattr(spanner, '_slicing_metersFound')
         result.append('>>')
      return result

   ##FIXME: formatting is ridiculously slow. 
   ##       find a way to make it faster.
   ## Tue Jan 13 12:05:43 EST 2009 [VA] using _slicing_metersFound boolean
   ## flag now to improve performance time. Better but still not perfect. 
   ## Is metric grid a good candidate for the UpdateInterface?

   def _before(self, leaf):
      '''Spanner format contribution before leaf.'''
      from abjad.components.Container import Container
      from abjad.components.Skip import Skip
      result = [ ]
      spanner = self.spanner
      if not spanner.hide:
         #meter = spanner._matching_meter(leaf)
         matching_meter = spanner._matching_meter(leaf)
         if matching_meter is None:
            meter = None
         else:
            meter, temp_hide = matching_meter
         #if meter and not getattr(meter, '_temp_hide', False):
         if meter and not temp_hide:
            result.append(meter.format)
         #m = spanner._slicing_meters(leaf)
         m = spanner._slicing_meters(leaf)
         #m = [meter for meter in m if not getattr(meter, '_temp_hide', False)]
         m = [triple for triple in m if not triple[-1]]
         if m:
            ## set spanner._slicing_metersFound as temporary flag so that 
            ## spanner._after does not have to recompute _slicing_meters( )
            spanner._slicing_metersFound = True
            result.append('<<')
            for meter, moffset, temp_hide in m:
               s = Skip(Rational(1))
               #s.duration.multiplier = meter.offset - leaf.offset.start
               s.duration.multiplier = moffset - leaf.offset.start
               #s.meter.forced = meter
               numerator, denominator = meter.numerator, meter.denominator
               mark = marktools.TimeSignatureMark(numerator, denominator)(s)
               mark._is_cosmetic_mark = True
               container = Container([s])
               result.append(container.format)
      return result
