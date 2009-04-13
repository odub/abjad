from abjad import *


def test_containertools_contents_reverse_01( ):
   '''Retrograde works on a depth-0 Container with no spanners and no parent.'''

   t = Staff(construct.scale(8))
   leaves_rev = reversed(t.leaves)
   containertools.contents_reverse(t)

   assert list(leaves_rev) == t.leaves
   assert check.wf(t)


def test_containertools_contents_reverse_02( ):
   '''Retrograde works on a depth-0 Container with 
      one spanner attached and no parent.'''

   t = Staff(construct.scale(8))
   beam = Beam(t)
   leaves_rev = reversed(t.leaves)
   containertools.contents_reverse(t)

   assert list(leaves_rev) == t.leaves
   assert beam.components == [t]
   assert check.wf(t)


def test_containertools_contents_reverse_03( ):
   '''Retrograde works on a depth-0 Container 
      with one spanner attached to its leaves and with no parent.'''

   t = Staff(construct.scale(8))
   beam = Beam(t.leaves)
   leaves_rev = reversed(t.leaves)
   containertools.contents_reverse(t)

   assert list(leaves_rev) == t.leaves
   assert beam.components == t.leaves
   assert check.wf(t)


def test_containertools_contents_reverse_04( ):
   '''Retrograde works on a depth-0 Container with one spanner 
      attached to itself and with a parent.'''

   t = Staff([DynamicMeasure(construct.scale(8))] + construct.run(2))
   beam = Beam(t[0])
   leaves_rev = reversed(t[0].leaves)
   containertools.contents_reverse(t[0])
   assert list(leaves_rev) == t[0].leaves
   assert beam.components == [t[0]]
   assert check.wf(t)


def test_containertools_contents_reverse_05( ):
   '''Retrograde works on a depth-0 Container with one spanner 
      attached to its leaves and with a parent.'''

   t = Staff([DynamicMeasure(construct.scale(8))] + construct.run(2))
   beam = Beam(t[0].leaves)
   leaves_rev = reversed(t[0].leaves)
   containertools.contents_reverse(t[0])
   assert list(leaves_rev) == t[0].leaves
   assert beam.components == t[0].leaves
   assert check.wf(t)


def test_containertools_contents_reverse_06( ):
   '''Retrograde works on a depth-0 Container with one spanner 
      attached to its parent.'''

   t = Staff([DynamicMeasure(construct.scale(8))] + construct.scale(2))
   beam = Beam(t)
   leaves_rev = reversed(t[0].leaves)
   containertools.contents_reverse(t[0])
   assert list(leaves_rev) == t[0].leaves
   assert beam.components == [t]
   assert check.wf(t)


def test_containertools_contents_reverse_06( ):
   '''Retrograde works on a depth-0 Container with one spanner 
      attached to its parent's contents.'''

   notes = construct.scale(2)
   measure = DynamicMeasure(construct.scale(8))
   t = Staff([measure] + notes)
   beam = Beam(t[:])
   leaves_rev = reversed(t[0].leaves)
   containertools.contents_reverse(t[0])
   assert list(leaves_rev) == t[0].leaves
   assert beam.components == [measure] + notes
   assert check.wf(t)


def test_containertools_contents_reverse_07( ):
   '''Retrograde works on a depth-1 Container 
      with one spanner attached to its contents and with no parent.'''

   notes = construct.scale(2)
   measure = DynamicMeasure(construct.scale(8))
   t = Staff([measure] + notes)
   beam = Beam(t[:])
   containertools.contents_reverse(t)

   assert beam.components[0] == notes[1]
   assert beam.components[1] == notes[0]
   assert beam.components[2] == measure
   assert check.wf(t)


def test_containertools_contents_reverse_10( ):
   '''Retrograde works on a depth-2 Container with 
      no parent and with spanners at all levels.'''

   m1 = DynamicMeasure(construct.scale(4)) 
   m2 = DynamicMeasure(construct.scale(3))
   staff = Staff([m1, m2])
   pedal = PianoPedal(staff)
   trill = Trill(staff[:])
   beam1 = Beam(staff[0])
   beam2 = Beam(staff[1])
   gliss = Glissando(staff.leaves)
   containertools.contents_reverse(staff)
   assert staff[0] is m2
   assert staff[1] is m1
   assert len(m2) == 3
   assert len(m1) == 4
   assert pedal.components == [staff]
   assert trill.components == staff[:]
   assert beam1.components == [m1]
   assert beam2.components == [m2]
   assert gliss.components == staff.leaves
   assert check.wf(staff)
