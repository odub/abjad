# -*- encoding: utf-8 -*-
from abjad import *
import py.test


def test_GraceContainer_01():
    r'''Grace music is a container.
    '''

    gracecontainer = leaftools.GraceContainer([Note(0, (1, 16)), Note(2, (1, 16)), Note(4, (1, 16))])

    assert isinstance(gracecontainer, Container)
    assert len(gracecontainer) == 3
    assert testtools.compare(
        gracecontainer.lilypond_format,
        r'''
        \grace {
            c'16
            d'16
            e'16
        }
        '''
        )

    r'''
    \grace {
        c'16
        d'16
        e'16
    }
    '''


def test_GraceContainer_02():
    r'''GraceContainer.kind is managed attribute.
        GraceContainer.kind knows about "after", "grace",
        "acciaccatura", "appoggiatura"'''

    gracecontainer = leaftools.GraceContainer([Note(0, (1, 16)), Note(2, (1, 16)), Note(4, (1, 16))])
    gracecontainer.kind = 'acciaccatura'
    assert gracecontainer.kind == 'acciaccatura'
    gracecontainer.kind = 'grace'
    assert gracecontainer.kind == 'grace'
    gracecontainer.kind = 'after'
    assert gracecontainer.kind == 'after'
    gracecontainer.kind = 'appoggiatura'
    assert gracecontainer.kind == 'appoggiatura'
    assert py.test.raises(AssertionError, 'gracecontainer.kind = "blah"')


def test_GraceContainer_03():
    r'''Grace formats correctly as grace.
    '''

    gracecontainer = leaftools.GraceContainer(notetools.make_repeated_notes(3))
    gracecontainer.kind = 'grace'
    assert testtools.compare(
        gracecontainer.lilypond_format,
        r'''
        \grace {
            c'8
            c'8
            c'8
        }
        '''
        )

    r'''
    \grace {
        c'8
        c'8
        c'8
    }
    '''


def test_GraceContainer_04():
    r'''Grace formats correctly as acciaccatura.
    '''

    gracecontainer = leaftools.GraceContainer(notetools.make_repeated_notes(3))
    gracecontainer.kind = 'acciaccatura'
    assert testtools.compare(
        gracecontainer.lilypond_format,
        r'''
        \acciaccatura {
            c'8
            c'8
            c'8
        }
        '''
        )

    r'''
    \acciaccatura {
        c'8
        c'8
        c'8
    }
    '''


def test_GraceContainer_05():
    r'''Grace formats correctly as appoggiatura.
    '''

    gracecontainer = leaftools.GraceContainer(notetools.make_repeated_notes(3))
    gracecontainer.kind = 'appoggiatura'
    assert testtools.compare(
        gracecontainer.lilypond_format,
        r'''
        \appoggiatura {
            c'8
            c'8
            c'8
        }
        '''
        )

    r'''
    \appoggiatura {
        c'8
        c'8
        c'8
    }
    '''


def test_GraceContainer_06():
    r'''Grace formats correctly as after grace.
    '''

    gracecontainer = leaftools.GraceContainer(notetools.make_repeated_notes(3))
    gracecontainer.kind = 'after'
    assert testtools.compare(
        gracecontainer.lilypond_format,
        r'''
        {
            c'8
            c'8
            c'8
        }
        '''
        )

    r'''
    {
        c'8
        c'8
        c'8
    }
    '''


def test_GraceContainer_07():
    r'''Grace containers can be appended.
    '''

    gracecontainer = leaftools.GraceContainer(notetools.make_repeated_notes(2))
    n = Note(1, (1, 4))
    gracecontainer.append(n)
    assert len(gracecontainer) == 3
    assert gracecontainer[-1] is n


def test_GraceContainer_08():
    r'''Grace containers can be extended.
    '''

    gracecontainer = leaftools.GraceContainer(notetools.make_repeated_notes(2))
    ns = Note(1, (1, 4)) * 2
    gracecontainer.extend(ns)
    assert len(gracecontainer) == 4
    assert gracecontainer[-2:] == ns
