# -*- encoding: utf-8 -*-
from abjad import *


def test_Staff_time_signature_01():
    r'''Force time signature on nonempty staff.
    '''

    t = Staff(Note("c'4") * 8)
    contexttools.TimeSignatureMark((2, 4))(t)

    r'''
    \new Staff {
        \time 2/4
        c'4
        c'4
        c'4
        c'4
        c'4
        c'4
        c'4
        c'4
    }
    '''

    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff {
            \time 2/4
            c'4
            c'4
            c'4
            c'4
            c'4
            c'4
            c'4
            c'4
        }
        '''
        )


def test_Staff_time_signature_02():
    r'''Force time signature on empty staff.
    '''

    t = Staff([])
    contexttools.TimeSignatureMark((2, 4))(t)

    r'''
    \new Staff {
        \time 2/4
    }
    '''

    assert testtools.compare(
        t.lilypond_format,
        '\\new Staff {\n\t\\time 2/4\n}'
        )


def test_Staff_time_signature_03():
    r'''Staff time signature carries over to staff-contained leaves.
    '''

    t = Staff(Note("c'4") * 8)
    contexttools.TimeSignatureMark((2, 4))(t)
    for x in t:
        assert x.get_effective_context_mark(contexttools.TimeSignatureMark) \
            == contexttools.TimeSignatureMark((2, 4))


def test_Staff_time_signature_04():
    r'''Staff time signature set and then clear.
    '''

    t = Staff(Note("c'4") * 8)
    contexttools.TimeSignatureMark((2, 4))(t)
    t.get_effective_context_mark(contexttools.TimeSignatureMark).detach()
    for leaf in t:
        assert leaf.get_effective_context_mark(
            contexttools.TimeSignatureMark) is None
