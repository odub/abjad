from abjad import *


def test_RigidMeasure_meter_assignment_01( ):
   '''RigidMeasures allow meter reassignment.'''

   t = Measure((4, 8), macros.scale(4))

   r'''
   {
           \time 4/8
           c'8
           d'8
           e'8
           f'8
   }
   '''

   t.pop( )
   #t.meter.forced = metertools.Meter(3, 8)
   marktools.TimeSignatureMark(3, 8)(t)

   r'''
   {
           \time 3/8
           c'8
           d'8
           e'8
   }
   '''

   assert t.format == "{\n\t\\time 3/8\n\tc'8\n\td'8\n\te'8\n}"
