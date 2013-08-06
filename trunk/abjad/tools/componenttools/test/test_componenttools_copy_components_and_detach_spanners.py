# -*- encoding: utf-8 -*-
from abjad import *


def test_componenttools_copy_components_and_detach_spanners_01():
    r'''Withdraw components from spanners.
        Deepcopy unspanned components.
        Reapply spanners to components.
        Return unspanned copy.'''

    t = Voice(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)
    beam = spannertools.BeamSpanner(t[:2] + t[2][:] + t[3][:])
    slur = spannertools.SlurSpanner(t[0][:] + t[1][:] + t[2:])
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Voice {
        {
            \time 2/8
            c'8 [ (
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8 ] )
        }
    }
    '''

    result = componenttools.copy_components_and_detach_spanners([t])
    voice = result[0]
    measuretools.set_always_format_time_signature_of_measures_in_expr(voice)

    r'''
    \new Voice {
        {
            \time 2/8
            c'8
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8
        }
    }
    '''

    assert select(t).is_well_formed()
    assert select(voice).is_well_formed()
    assert testtools.compare(
        voice.lilypond_format,
        r'''
        \new Voice {
            {
                \time 2/8
                c'8
                d'8
            }
            {
                \time 2/8
                e'8
                f'8
            }
            {
                \time 2/8
                g'8
                a'8
            }
            {
                \time 2/8
                b'8
                c''8
            }
        }
        '''
        )


def test_componenttools_copy_components_and_detach_spanners_02():
    r'''Withdraw components from spanners.
        Deepcopy unspanned components.
        Reapply spanners to components.
        Return unspanned copy.'''

    t = Voice(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)
    beam = spannertools.BeamSpanner(t[:2] + t[2][:] + t[3][:])
    slur = spannertools.SlurSpanner(t[0][:] + t[1][:] + t[2:])
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Voice {
        {
            \time 2/8
            c'8 [ (
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8 ] )
        }
    }
    '''

    result = componenttools.copy_components_and_detach_spanners(t[1:])
    new = Voice(result)
    measuretools.set_always_format_time_signature_of_measures_in_expr(new)

    r'''
    \new Voice {
        {
            \time 2/8
            e'8
            f'8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8
        }
    }
    '''

    assert select(t).is_well_formed()
    assert select(new).is_well_formed()
    assert testtools.compare(
        new.lilypond_format,
        r'''
        \new Voice {
            {
                \time 2/8
                e'8
                f'8
            }
            {
                \time 2/8
                g'8
                a'8
            }
            {
                \time 2/8
                b'8
                c''8
            }
        }
        '''
        )


def test_componenttools_copy_components_and_detach_spanners_03():
    r'''Withdraw components from spanners.
    Deepcopy unspanned components.
    Reapply spanners to components.
    Return unspanned copy.
    '''

    t = Voice(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)
    beam = spannertools.BeamSpanner(t[:2] + t[2][:] + t[3][:])
    slur = spannertools.SlurSpanner(t[0][:] + t[1][:] + t[2:])
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Voice {
        {
            \time 2/8
            c'8 [ (
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8 ] )
        }
    }
    '''

    result = componenttools.copy_components_and_detach_spanners(t.select_leaves()[:6])
    new = Voice(result)
    measuretools.set_always_format_time_signature_of_measures_in_expr(new)

    r'''
    \new Voice {
        c'8
        d'8
        e'8
        f'8
        g'8
        a'8
    }
    '''

    assert select(t).is_well_formed()
    assert select(new).is_well_formed()
    assert testtools.compare(
        new.lilypond_format,
        r'''
        \new Voice {
            c'8
            d'8
            e'8
            f'8
            g'8
            a'8
        }
        '''
        )


def test_componenttools_copy_components_and_detach_spanners_04():
    r'''Withdraw components from spanners.
    Deepcopy unspanned components.
    Reapply spanners to components.
    Return unspanned copy.
    '''

    t = Voice(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)
    beam = spannertools.BeamSpanner(t[:2] + t[2][:] + t[3][:])
    slur = spannertools.SlurSpanner(t[0][:] + t[1][:] + t[2:])
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Voice {
        {
            \time 2/8
            c'8 [ (
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8 ] )
        }
    }
    '''

    result = componenttools.copy_components_and_detach_spanners(t[-2:])
    new = Voice(result)
    measuretools.set_always_format_time_signature_of_measures_in_expr(new)

    r'''
    \new Voice {
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8
        }
    }
    '''

    assert select(t).is_well_formed()
    assert select(new).is_well_formed()
    assert testtools.compare(
        new.lilypond_format,
        r'''
        \new Voice {
            {
                \time 2/8
                g'8
                a'8
            }
            {
                \time 2/8
                b'8
                c''8
            }
        }
        '''
        )


def test_componenttools_copy_components_and_detach_spanners_05():
    r'''Withdraw components from spanners.
    Deepcopy unspanned components.
    Reapply spanners to components.
    Return unspanned copy.
    Use optional 'n' argument for multiple copies.
    '''

    t = Voice(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)
    beam = spannertools.BeamSpanner(t[:2] + t[2][:] + t[3][:])
    slur = spannertools.SlurSpanner(t[0][:] + t[1][:] + t[2:])
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Voice {
        {
            \time 2/8
            c'8 [ (
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8 ] )
        }
    }
    '''

    result = componenttools.copy_components_and_detach_spanners(t[-2:], 3)
    new = Voice(result)
    measuretools.set_always_format_time_signature_of_measures_in_expr(new)

    r'''
    \new Voice {
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8
        }
    }
    '''

    assert select(new).is_well_formed()
    assert testtools.compare(
        new.lilypond_format,
        r'''
        \new Voice {
            {
                \time 2/8
                g'8
                a'8
            }
            {
                \time 2/8
                b'8
                c''8
            }
            {
                \time 2/8
                g'8
                a'8
            }
            {
                \time 2/8
                b'8
                c''8
            }
            {
                \time 2/8
                g'8
                a'8
            }
            {
                \time 2/8
                b'8
                c''8
            }
        }
        '''
        )
