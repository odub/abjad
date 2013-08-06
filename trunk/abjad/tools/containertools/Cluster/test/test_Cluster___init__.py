# -*- encoding: utf-8 -*-
from abjad import *


def test_Cluster___init___01():
    r'''Cluster can be empty.
    '''
    t = containertools.Cluster([])
    assert not t.is_parallel
    assert len(t) == 0
    assert testtools.compare(
        t.lilypond_format,
        '\\makeClusters {\n}'
        )


def test_Cluster___init___02():
    t = containertools.Cluster(Note(1, (1, 4)) * 4)
    assert isinstance(t, containertools.Cluster)
    assert not t.is_parallel
    assert len(t) == 4
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \makeClusters {
            cs'4
            cs'4
            cs'4
            cs'4
        }
        '''
        )
