# -*- encoding: utf-8 -*-
from abjad import *


def test_Staff_engraver_consists_01():

    t = Staff("c'8 d'8 e'8 f'8")
    t.engraver_consists.append('Horizontal_bracket_engraver')
    t.engraver_consists.append('Instrument_name_engraver')

    r'''
    \new Staff \with {
        \consists Horizontal_bracket_engraver
        \consists Instrument_name_engraver
    } {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            \consists Horizontal_bracket_engraver
            \consists Instrument_name_engraver
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )
