# -*- encoding: utf-8 -*-
from abjad import *


def test_Spanner_fracture_01():
    r'''Fracture container spanner to the right of index 1.
    '''

    t = Staff(Container(notetools.make_repeated_notes(4)) * 3)
    pitchtools.set_ascending_named_chromatic_pitches_on_tie_chains_in_expr(t)
    p = spannertools.BeamSpanner(t[:])
    original, left, right = p.fracture(1, direction=Right)

    assert len(original.components) == 3
    assert original.components[0] is t[0]
    assert original.components[1] is t[1]
    assert original.components[2] is t[2]
    assert len(original.leaves) == 12

    assert len(left.components) == 2
    assert left.components[0] is t[0]
    assert left.components[1] is t[1]
    assert len(left.leaves) == 8

    assert len(right.components) == 1
    assert right.components[0] is t[2]
    assert len(right.leaves) == 4

    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff {
            {
                c'8 [
                cs'8
                d'8
                ef'8
            }
            {
                e'8
                f'8
                fs'8
                g'8 ]
            }
            {
                af'8 [
                a'8
                bf'8
                b'8 ]
            }
        }
        '''
        )

    r'''
    \new Staff {
        {
            c'8 [
            cs'8
            d'8
            ef'8
        }
        {
            e'8
            f'8
            fs'8
            g'8 ]
        }
        {
            af'8 [
            a'8
            bf'8
            b'8 ]
        }
    }
    '''
