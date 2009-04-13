from abjad import *
import py.test


def test_measuretools_scale_and_remeter_01( ):
   '''Scale binary to nonbinary.
      No notehead rewriting necessary.'''

   t = RigidMeasure((3, 8), construct.scale(3))
   measuretools.scale_and_remeter(t, Rational(2, 3))

   r'''\time 3/12
        \scaleDurations #'(2 . 3) {
                c'8
                d'8
                e'8
        }'''

   assert check.wf(t)
   assert t.format == "\t\\time 3/12\n\t\\scaleDurations #'(2 . 3) {\n\t\tc'8\n\t\td'8\n\t\te'8\n\t}"


def test_measuretools_scale_and_remeter_02( ):
   '''Scale nonbinary meter to binary. 
      No notehead rewriting necessary.'''
  
   t = RigidMeasure((3, 12), construct.scale(3))
   measuretools.scale_and_remeter(t, Rational(3, 2))

   r'''\time 3/8
        c'8
        d'8
        e'8'''

   assert check.wf(t)
   assert t.format == "\t\\time 3/8\n\tc'8\n\td'8\n\te'8"


def test_measuretools_scale_and_remeter_03( ):
   '''Scale binary meter to binary meter. 
      Noteheads rewrite with dots.'''

   t = RigidMeasure((3, 8), construct.scale(3))
   measuretools.scale_and_remeter(t, Rational(3, 2))

   r'''\time 9/16
        c'8.
        d'8.
        e'8.'''

   assert check.wf(t)
   assert t.format == "\t\\time 9/16\n\tc'8.\n\td'8.\n\te'8."


def test_measuretools_scale_and_remeter_04( ):
   '''Scale binary meter to binary meter.
      Noteheads rewrite without dots.'''

   t = RigidMeasure((9, 16), construct.scale(3, Rational(3, 16)))
   measuretools.scale_and_remeter(t, Rational(2, 3))

   r'''\time 3/8
        c'8
        d'8
        e'8'''

   assert check.wf(t)
   assert t.format == "\t\\time 3/8\n\tc'8\n\td'8\n\te'8"


def test_measuretools_scale_and_remeter_05( ):
   '''Scale binary meter to nonbinary meter.
      No notehead rewriting necessary.'''

   t = RigidMeasure((9, 16), construct.scale(9, Rational(1, 16)))
   measuretools.scale_and_remeter(t, Rational(2, 3))

   r'''\time 9/24
        \scaleDurations #'(2 . 3) {
                c'16
                d'16
                e'16
                f'16
                g'16
                a'16
                b'16
                c''16
                d''16
        }'''

   assert check.wf(t)
   assert t.format == "\t\\time 9/24\n\t\\scaleDurations #'(2 . 3) {\n\t\tc'16\n\t\td'16\n\t\te'16\n\t\tf'16\n\t\tg'16\n\t\ta'16\n\t\tb'16\n\t\tc''16\n\t\td''16\n\t}"


def test_measuretools_scale_and_remeter_06( ):
   '''Scale nonbinary meter to binary meter.
      Noteheads rewrite with double duration.'''

   t = RigidMeasure((3, 12), construct.scale(3))
   measuretools.scale_and_remeter(t, Rational(3))

   r'''\time 3/4
        c'4
        d'4
        e'4'''

   assert check.wf(t)
   assert t.format == "\t\\time 3/4\n\tc'4\n\td'4\n\te'4"


def test_measuretools_scale_and_remeter_07( ):
   '''Scale binary meter by one half.
      Noteheads rewrite with half duration.
      Meter rewrites with double denominator.'''

   t = RigidMeasure((6, 16), construct.scale(6, Rational(1, 16)))
   measuretools.scale_and_remeter(t, Rational(1, 2))

   r'''\time 6/32
           c'32
           d'32
           e'32
           f'32
           g'32
           a'32'''

   assert check.wf(t)
   assert t.format == "\t\\time 6/32\n\tc'32\n\td'32\n\te'32\n\tf'32\n\tg'32\n\ta'32"


def test_measuretools_scale_and_remeter_08( ):
   '''Scale binary meter by one quarter.
      Noteheads rewrite with quarter duration.
      Meter rewrites with quadruple denominator.'''

   t = RigidMeasure((6, 16), construct.scale(6, Rational(1, 16)))
   measuretools.scale_and_remeter(t, Rational(1, 4))

   r'''\time 6/64
           c'64
           d'64
           e'64
           f'64
           g'64
           a'64'''

   assert check.wf(t)
   assert t.format == "\t\\time 6/64\n\tc'64\n\td'64\n\te'64\n\tf'64\n\tg'64\n\ta'64"


def test_measuretools_scale_and_remeter_09( ):
   '''Scale binary meter by two.
      Noteheads rewrite with double duration.
      Meter rewrites with half denominator.'''

   t = RigidMeasure((6, 16), construct.scale(6, Rational(1, 16)))
   measuretools.scale_and_remeter(t, Rational(2))

   r'''\time 6/8
        c'8
        d'8
        e'8
        f'8
        g'8
        a'8'''

   assert check.wf(t)
   assert t.format == "\t\\time 6/8\n\tc'8\n\td'8\n\te'8\n\tf'8\n\tg'8\n\ta'8"


def test_measuretools_scale_and_remeter_10( ):
   '''Scale binary meter by four.
      Noteheads rewrite with quadruple duration.
      Meter rewrites with quarter denominator.'''

   t = RigidMeasure((6, 16), construct.scale(6, Rational(1, 16)))
   measuretools.scale_and_remeter(t, Rational(4))

   r'''\time 6/4
        c'4
        d'4
        e'4
        f'4
        g'4
        a'4'''

   assert check.wf(t)
   assert t.format == "\t\\time 6/4\n\tc'4\n\td'4\n\te'4\n\tf'4\n\tg'4\n\ta'4"


def test_measuretools_scale_and_remeter_11( ):
   '''Raise ZeroDivisionError when multiplier equals zero.'''

   t = RigidMeasure((6, 16), construct.scale(6, Rational(1, 16)))
   py.test.raises(ZeroDivisionError, 'measuretools.scale_and_remeter(t, 0)')
