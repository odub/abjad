# -*- encoding: utf-8 -*-
from abjad import *
import py.test


def test_Measure_duration_01():
    r'''Properly filled Measure with power-of-two time signature denominator.
    '''

    t = Measure((3, 8), "c'8 d'8 e'8")

    r'''
    {
        \time 3/8
        c'8
        d'8
        e'8
    }
    '''

    assert t._contents_duration == Duration(3, 8)
    assert t._preprolated_duration == Duration(3, 8)
    assert t.get_duration() == Duration(3, 8)

    assert testtools.compare(
        t.lilypond_format,
        r'''
        {
            \time 3/8
            c'8
            d'8
            e'8
        }
        '''
        )


def test_Measure_duration_02():
    r'''Properly filled measure without power-of-two time signature denominator.
    '''

    t = Measure((3, 10), "c'8 d'8 e'8")

    r'''
    {
        \time 3/10
        \scaleDurations #'(4 . 5) {
            c'8
            d'8
            e'8
        }
    }
    '''

    assert t._contents_duration == Duration(3, 8)
    assert t._preprolated_duration == Duration(3, 10)
    assert t.get_duration() == Duration(3, 10)

    assert testtools.compare(
        t.lilypond_format,
        r'''
        {
            \time 3/10
            \scaleDurations #'(4 . 5) {
                c'8
                d'8
                e'8
            }
        }
        '''
        )



def test_Measure_duration_03():
    r'''Improperly filled measure without power-of-two time signature denominator.
    '''

    t = Measure((3, 8), "c'8 d'8 e'8 f'8")

    assert py.test.raises(OverfullContainerError, 't.lilypond_format')

    assert t._contents_duration == Duration(4, 8)
    assert t._preprolated_duration == Duration(4, 8)
    assert t.get_duration() == Duration(4, 8)


def test_Measure_duration_04():
    r'''Impropely filled measure without power-of-two time signature denominator.
    '''

    t = Measure((3, 10), "c'8 d'8 e'8 f'8")

    assert py.test.raises(OverfullContainerError, 't.lilypond_format')

    assert t._contents_duration == Duration(4, 8)
    assert t._preprolated_duration == Duration(4, 10)
    assert t.get_duration() == Duration(4, 10)
