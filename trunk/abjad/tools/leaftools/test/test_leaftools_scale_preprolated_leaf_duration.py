# -*- encoding: utf-8 -*-
from abjad import *


def test_leaftools_scale_preprolated_leaf_duration_01():

    t = Note("c'4")
    leaftools.scale_preprolated_leaf_duration(t, Duration(1, 2))
    assert t.lilypond_format == "c'8"


def test_leaftools_scale_preprolated_leaf_duration_02():

    t = Note("c'4")
    leaftools.scale_preprolated_leaf_duration(t, Duration(2))
    assert t.lilypond_format == "c'2"


def test_leaftools_scale_preprolated_leaf_duration_03():

    staff = Staff("c'8 d'8 e'8 f'8")
    spannertools.BeamSpanner(staff.select_leaves())
    leaftools.scale_preprolated_leaf_duration(staff[1], Duration(5, 4))

    r'''
    \new Staff {
      c'8 [
      d'8 ~
      d'32
      e'8
      f'8 ]
    }
    '''

    assert testtools.compare(
        staff.lilypond_format,
        r'''
        \new Staff {
            c'8 [
            d'8 ~
            d'32
            e'8
            f'8 ]
        }
        '''
        )


def test_leaftools_scale_preprolated_leaf_duration_04():

    staff = Staff("c'8 d'8 e'8 f'8")
    spannertools.BeamSpanner(staff.select_leaves())
    leaftools.scale_preprolated_leaf_duration(staff[1], Duration(2, 3))

    r'''
    \new Staff {
      c'8 [
      \times 2/3 {
            d'8
      }
      e'8
      f'8 ]
    }
    '''

    assert testtools.compare(
        staff.lilypond_format,
        r'''
        \new Staff {
            c'8 [
            \times 2/3 {
                d'8
            }
            e'8
            f'8 ]
        }
        '''
        )
