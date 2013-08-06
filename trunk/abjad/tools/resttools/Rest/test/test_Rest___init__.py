# -*- encoding: utf-8 -*-
from abjad import *


def test_Rest___init___01():
    r'''Init rest from LilyPond input string.
    '''

    rest = Rest('r8.')

    assert rest.written_duration == Duration(3, 16)


def test_Rest___init___02():
    r'''Init rest from written duration and LilyPond multiplier.
    '''

    rest = Rest(Duration(1, 4), Duration(1, 2))

    assert rest.lilypond_format == 'r4 * 1/2'


def test_Rest___init___03():
    r'''Init rest from other rest.
    '''

    rest_1 = Rest((1, 4), (1, 2))
    rest_1.override.staff.note_head.color = 'red'
    rest_2 = Rest(rest_1)

    assert isinstance(rest_1, Rest)
    assert isinstance(rest_2, Rest)
    assert rest_1.lilypond_format == rest_2.lilypond_format
    assert rest_1 is not rest_2


def test_Rest___init___04():
    r'''Init rest from containerized chord.
    '''

    c = Chord([2, 3, 4], (1, 4))
    duration = c.written_duration
    r = Rest(c)
    assert isinstance(r, Rest)
    # check that attributes have not been removed or added.
    assert dir(c) == dir(Chord([2, 3, 4], (1, 4)))
    assert dir(r) == dir(Rest((1, 4)))
    assert r._parent is None
    assert r.written_duration == duration


def test_Rest___init___05():
    r'''Init rest from tupletized chord.
    '''

    t = tuplettools.FixedDurationTuplet(Duration(2, 8), Chord([2, 3, 4], (1, 4)) * 3)
    d = t[0].written_duration
    rest = Rest(t[0])
    assert isinstance(rest, Rest)
    assert isinstance(t[0], Chord)
    assert t[0]._parent is t
    assert rest._parent is None


def test_Rest___init___06():
    r'''Init rest from beamed chord.
    '''

    staff = Staff(Chord([2, 3, 4], (1, 4)) * 3)
    spannertools.BeamSpanner(staff[:])
    rest = Rest(staff[0])
    assert isinstance(rest, Rest)
    assert isinstance(staff[0], Chord)
    assert staff[0]._parent is staff
    assert rest._parent is None


def test_Rest___init___07():
    r'''Init rest from skip.
    '''

    s = skiptools.Skip((1, 8))
    d = s.written_duration
    r = Rest(s)
    assert isinstance(r, Rest)
    assert dir(s) == dir(skiptools.Skip((1, 4)))
    assert dir(r) == dir(Rest((1, 4)))
    assert r._parent is None
    assert r.written_duration == d


def test_Rest___init___08():
    r'''Init rest from tupletted skip.
    '''

    t = tuplettools.FixedDurationTuplet(Duration(2, 8), skiptools.Skip((1, 8)) * 3)
    d = t[0].written_duration
    rest = Rest(t[0])
    assert isinstance(t[0], skiptools.Skip)
    assert isinstance(rest, Rest)
    assert t[0]._parent is t
    assert t[0].written_duration == d
    assert rest._parent is None


def test_Rest___init___09():
    r'''Init rest from beamed skip.
    '''

    t = Staff([Note(0, (1, 8)), skiptools.Skip((1, 8)), Note(0, (1, 8))])
    spannertools.BeamSpanner(t[:])
    rest = Rest(t[1])
    assert isinstance(t[1], skiptools.Skip)
    assert t[1] in t
    assert isinstance(rest, Rest)
    assert rest not in t


def test_Rest___init___10():
    r'''Init rest from unincorporated note.
    '''

    n = Note(2, (1, 8))
    d = n.written_duration
    r = Rest(n)
    assert isinstance(r, Rest)
    # check that attributes have not been removed or added.
    assert dir(n) == dir(Note(0, (1, 8)))
    assert dir(r) == dir(Rest((1, 4)))
    assert r.lilypond_format == 'r8'
    assert r._parent is None
    assert r.written_duration == d


def test_Rest___init___11():
    r'''Init rest from tupletized note.
    '''

    t = tuplettools.FixedDurationTuplet(Duration(2, 8), Note(0, (1, 8)) * 3)
    d = t[0].written_duration
    rest = Rest(t[0])
    assert isinstance(t[0], Note)
    assert isinstance(rest, Rest)
    assert t[0]._parent is t
    assert t[0].written_duration == d
    assert rest._parent is None


def test_Rest___init___12():
    r'''Init rest from beamed note.
    '''

    t = Staff(Note(0, (1, 8)) * 3)
    spannertools.BeamSpanner(t[:])
    rest = Rest(t[0])
    assert isinstance(t[0], Note)
    assert isinstance(rest, Rest)
    assert t[0]._parent is t
    assert rest._parent is None


def test_Rest___init___13():
    r'''Init rest from spanned note.
    '''

    t = Voice("c'8 d'8 e'8 f'8")
    spannertools.BeamSpanner(t[:])
    rest = Rest(t[-1])
    componenttools.move_parentage_and_spanners_from_components_to_components(t[-1:], [rest])

    r'''
    \new Voice {
        c'8 [
        d'8
        e'8
        r8 ]
    }
    '''

    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Voice {
            c'8 [
            d'8
            e'8
            r8 ]
        }
        '''
        )


def test_Rest___init___14():
    r'''Init multiple rests from spanned notes.
    '''

    t = Voice("c'8 d'8 e'8 f'8")
    spannertools.BeamSpanner(t[:])
    for note in t:
        rest = Rest(note)
        componenttools.move_parentage_and_spanners_from_components_to_components([note], [rest])

    r'''
    \new Voice {
        r8 [
        r8
        r8
        r8 ]
    }
    '''

    assert testtools.compare(
        t.lilypond_format,
        '\\new Voice {\n\tr8 [\n\tr8\n\tr8\n\tr8 ]\n}'
        )
