from abjad import *


def test_pitchtools_chromatic_interval_from_to_01( ):

   pitch_1 = Pitch(10)
   pitch_2 = Pitch(12)

   chromatic_interval = pitchtools.chromatic_interval_from_to(pitch_1, pitch_2)
   assert chromatic_interval == pitchtools.ChromaticInterval(2)

   chromatic_interval = pitchtools.chromatic_interval_from_to(pitch_2, pitch_1)
   assert chromatic_interval == pitchtools.ChromaticInterval(-2)

   chromatic_interval = pitchtools.chromatic_interval_from_to(pitch_1, pitch_1)
   assert chromatic_interval == pitchtools.ChromaticInterval(0)

   chromatic_interval = pitchtools.chromatic_interval_from_to(pitch_2, pitch_2)
   assert chromatic_interval == pitchtools.ChromaticInterval(0)
